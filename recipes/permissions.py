from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import NotFound

class HasUserPermission(BasePermission):
    # def has_object_permission(self, request, view, obj):
    #     import pdb ; pdb.set_trace()
    #     if request.method in SAFE_METHODS:
    #         return True

    #     return request.user.id == obj.owner.id

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        
        try:
            obj = view.get_object()
        except NotFound:
            return False

        if obj.user == request.user:
            return True

        return False