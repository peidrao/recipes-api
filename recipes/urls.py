from django.urls import path, include
from rest_framework import routers



from .views import TagViewSet

router = routers.DefaultRouter()

router.register(r'api/v1/tags', TagViewSet, basename='tags')

urlpatterns = [
     path('', include(router.urls)),
]

