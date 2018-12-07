from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsSuperUserOrIsOwnerOrReadOnly(IsOwnerOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return super(IsSuperUserOrIsOwnerOrReadOnly, self).has_object_permission(request, view, obj)
