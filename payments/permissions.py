from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request

class IsOwnPaymentMethod(BasePermission):
    def has_object_permission(self, request: Request, view, obj):
        return request.user.id == obj.user.id
