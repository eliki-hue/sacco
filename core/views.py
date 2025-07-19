from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets , generics, permissions
from .models import MemberProfile, Contribution, Loan, Repayment
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken



class MemberProfileViewSet(viewsets.ModelViewSet):
    queryset = MemberProfile.objects.all()
    serializer_class = MemberProfileSerializer

class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class RepaymentViewSet(viewsets.ModelViewSet):
    queryset = Repayment.objects.all()
    serializer_class = RepaymentSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IsOwnerOrAdminMixin:
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return self.model_class.objects.all()
        profile = MemberProfile.objects.get(user=user)
        return self.model_class.objects.filter(member=profile)

class ContributionViewSet(IsOwnerOrAdminMixin, viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer
    permission_classes = [IsAuthenticated]
    model_class = Contribution

class LoanViewSet(IsOwnerOrAdminMixin, viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]
    model_class = Loan

class RepaymentViewSet(viewsets.ModelViewSet):
    queryset = Repayment.objects.all()
    serializer_class = RepaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Repayment.objects.all()
        profile = MemberProfile.objects.get(user=user)
        return Repayment.objects.filter(loan__member=profile)


class CookieTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        data = response.data

        refresh = RefreshToken(data['refresh'])
        access_token = str(refresh.access_token)

        res = Response({"message": "Login successful"})
        res.set_cookie(
            key='access_token',
            value=access_token,
            httponly=True,
            secure=True,  # only over HTTPS
            samesite='Lax'
        )
        return res
    

class LogoutView(APIView):
    def post(self, request):
        response = Response({"message": "Logged out"})
        response.delete_cookie('access_token')
        return response
