from rest_framework import permissions

from .models import ReviewRecipe

class HasOnlyReview(permissions.BasePermission):
    message = 'You can only rate a recipe once'
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        if ReviewRecipe.objects.filter(user=request.user, recipe_id=request.data['recipe']).count() >= 1:
            return False
        return True
        