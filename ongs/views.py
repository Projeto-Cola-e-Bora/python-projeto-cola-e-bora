from django.shortcuts import get_object_or_404

from rest_framework import views
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from .models import Ong
from .serializers import OngSerializer, OngSerializerToAdm
from .permissions import (
    IsAuthenticatedOrListOnly,
    IsOwnOngOrRetrieveOnly,
)

from users.models import User
from users.serializers import UserSerializer
from events.models import Event
from events.serializers import EventSerializer, AllEventsSerializer


class OngView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrListOnly]

    queryset = Ong.objects.all()
    serializer_class = OngSerializer

    def perform_create(self, serializer):
        user = self.request.user
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return serializer.save(user=user)

    def create(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return Response(
                {"detail": "This user already have a ONG created"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().create(request, *args, **kwargs)


class OngDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnOngOrRetrieveOnly]

    queryset = Ong.objects.all()
    serializer_class = OngSerializerToAdm

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        instance = self.get_object()
        if instance.user.id != user.id:
            serializer = OngSerializer(instance)
            return Response(serializer.data)

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_destroy(self, instance):
        user = User.objects.get(pk=instance.user.id)
        user.is_staff = False
        user.is_superuser = False
        user.save()
        instance.delete()


class OngEventUsersView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        if event.ong.id != request.user.ong.id:
            return views.Response(
                {"detail": "You do not have access"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        event_serializer = AllEventsSerializer(event)
        users_serializer = UserSerializer(event.volunteers, many=True)
        response_data = {
            **event_serializer.data,
            "volunteers": [*users_serializer.data],
        }

        return views.Response(response_data, status=status.HTTP_200_OK)
