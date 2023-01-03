from rest_framework.permissions import BasePermission
from rest_framework import permissions
from rest_framework.request import Request


class IsAdmOrCreateOnly(BasePermission):
    def has_permission(self, request: Request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_superuser

        return True


class IsOwnOng(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.user.id
