from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required         

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name="login"),
    # CSRF endpoint
    path("csrf/", ensure_csrf_cookie(lambda request: JsonResponse({"detail": "CSRF cookie set"}))),

    # Auth check endpoint
    path("auth-check/", login_required(lambda request: JsonResponse({"authenticated": True}))),

]


router = DefaultRouter()
router.register(r'members', MemberProfileViewSet)
router.register(r'contributions', ContributionViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'repayments', RepaymentViewSet)

urlpatterns += router.urls