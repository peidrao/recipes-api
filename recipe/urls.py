from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from authentication.views import UserViewSet

router = routers.DefaultRouter()


router.register(r'api/v1/users', UserViewSet, basename='users')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('recipes.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('silk/', include('silk.urls', namespace='silk'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
