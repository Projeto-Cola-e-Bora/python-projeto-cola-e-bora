from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Ong
from .serializers import OngSerializer
from .permissions import IsAdmOrCreateOnly


class OngView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdmOrCreateOnly]

    queryset = Ong.objects.all()
    serializer_class = OngSerializer
