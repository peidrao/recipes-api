from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from authentication.views import UserViewSet
from recipes.views import IngredientViewSet, RecipeCreateView, RecipeDetailView, TagDetailView, TagListCreateView

router = routers.DefaultRouter()

# router.register(r'api/v1/tags', TagViewSet, basename='tags')
router.register(r'api/v1/users', UserViewSet, basename='users')
router.register(r'api/v1/ingredients', IngredientViewSet, basename='ingredients')
# router.register(r'api/v1/recipes', RecipeViewSet, basename='recipes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include(router.urls)),
    path('api/v1/recipes/', RecipeCreateView.as_view()),
    path('api/v1/recipes/<int:id>', RecipeDetailView.as_view()),
    path('api/v1/tags/', TagListCreateView.as_view()),
    path('api/v1/tags/<int:id>', TagDetailView.as_view()),
    # path('api/v1/categories/', CategoryListView.as_view()),

    path('api-auth/', include('rest_framework.urls')),
    path('silk/', include('silk.urls', namespace='silk'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
