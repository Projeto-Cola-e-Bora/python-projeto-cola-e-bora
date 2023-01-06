from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS
from rest_framework.request import Request

from events.models import Event


class IsAuthenticatedOrListOnly(BasePermission):
    def has_permission(self, request: Request, view):
        return request.method in SAFE_METHODS or bool(
            request.user and request.user.is_authenticated
        )


class IsOwnOngOrRetrieveOnly(BasePermission):
    def has_object_permission(self, request: Request, view, obj):
        return request.method in SAFE_METHODS or request.user.id == obj.user.id
