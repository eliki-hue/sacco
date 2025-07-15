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
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)
    member_id = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'phone', 'member_id']

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        phone = validated_data['phone']
        member_id = validated_data['member_id']

        user = User.objects.create_user(username=username, email=email, password=password)
        MemberProfile.objects.create(user=user, phone=phone, member_id=member_id) # adding phone and id to the user to create a profile
        return user