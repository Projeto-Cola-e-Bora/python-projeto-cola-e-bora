from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsOwnerOrDonateOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return request.user.id == obj.ong.user.id

        return request.user.id != obj.ong.user.id
