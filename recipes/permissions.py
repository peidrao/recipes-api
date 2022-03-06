from rest_framework.permissions import BasePermission, SAFE_METHODS


class HasUserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        import pdb ; pdb.set_trace()
        if request.method in SAFE_METHODS:
            return True

        return request.user.id == obj.owner.id