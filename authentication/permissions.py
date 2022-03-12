from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    def has_object_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
      
        if request.method == 'POST':

            if request.user.is_superuser:
                return True
        
        return False
    
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        
        return False
