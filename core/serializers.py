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
