from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

from .models import Ong
from .serializers import OngSerializer, OngSerializerToAdm
from .permissions import IsAuthenticatedOrListOnly, IsOwnOngOrRetrieveOnly

from users.models import User


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
