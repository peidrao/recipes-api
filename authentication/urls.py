from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import ChangePasswordViewSet, TokenIsValidViewSet

urlpatterns = [
     path('api/v1/change_password/', ChangePasswordViewSet.as_view(), name="change_password"),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path("api/v1/token_is_valid/", TokenIsValidViewSet.as_view(), name='token_is_valid'),
]