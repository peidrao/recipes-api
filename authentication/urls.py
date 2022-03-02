from django.urls import path, include
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserViewSet, ChangePasswordViewSet, TokenIsValidViewSet

router = routers.DefaultRouter()

router.register(r'api/v1/users', UserViewSet, basename='user')

urlpatterns = [
     path('', include(router.urls)),
     path('api/v1/change_password/', ChangePasswordViewSet.as_view(), name="change_password"),
     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path("api/v1/token_is_valid/", TokenIsValidViewSet.as_view(), name='token_is_valid'),
]

