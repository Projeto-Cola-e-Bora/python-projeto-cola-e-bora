from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsAdmOrCreateOnly(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_superuser

        return True
