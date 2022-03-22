from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls', namespace='authentication')),
    path('', include('recipes.urls', namespace='recipes')),
    path('', include('reviews.urls', namespace='reviews')),
    path('api-auth/', include('rest_framework.urls')),
    path('silk/', include('silk.urls', namespace='silk'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
