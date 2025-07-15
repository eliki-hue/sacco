from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MemberProfile, Contribution, Loan, Repayment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MemberProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = MemberProfile
        fields = '__all__'

class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class RepaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repayment
        fields = '__all__'



# For registering a new user + profile
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)
    national_id = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    middle_name = serializers.CharField(write_only=True, allow_blank=True)
    last_name = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password',
            'first_name', 'middle_name', 'last_name',
            'phone', 'national_id'
        ]

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username is already taken.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already registered.")
        return value

    def validate_phone(self, value):
        if MemberProfile.objects.filter(phone=value).exists():
            raise serializers.ValidationError("Phone number is already registered.")
        return value

    def validate_national_id(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("National ID must be numeric.")
        if MemberProfile.objects.filter(national_id=value).exists():
            raise serializers.ValidationError("This national ID is already registered.")
        return value

    def create(self, validated_data):
        phone = validated_data.pop('phone')
        national_id = validated_data.pop('national_id')
        middle_name = validated_data.pop('middle_name')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        MemberProfile.objects.create(
            user=user,
            phone=phone,
            national_id=national_id,
            middle_name=middle_name
        )
        return user