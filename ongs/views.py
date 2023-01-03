from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Ong
from .serializers import OngSerializer
from .permissions import IsAdmOrCreateOnly, IsOwnOng


class OngView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmOrCreateOnly]

    queryset = Ong.objects.all()
    serializer_class = OngSerializer

    def perform_create(self, serializer):
        user = self.request.user
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return serializer.save(user=user)


class OngDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnOng]

    queryset = Ong.objects.all()
    serializer_class = OngSerializer
