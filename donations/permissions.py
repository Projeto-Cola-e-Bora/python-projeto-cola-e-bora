from django.shortcuts import get_object_or_404

from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from uuid import UUID

from ongs.models import Ong


class IsOwnerOrDonateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        pk = str(view.kwargs["pk"])
        ong = get_object_or_404(Ong, pk=pk)

        if request.method in SAFE_METHODS:
            return request.user == ong.user

        return request.user != ong.user
