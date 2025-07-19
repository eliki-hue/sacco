from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('api/token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),

]


router = DefaultRouter()
router.register(r'members', MemberProfileViewSet)
router.register(r'contributions', ContributionViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'repayments', RepaymentViewSet)

urlpatterns += router.urls