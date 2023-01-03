from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserOwner
from rest_framework.views import APIView, Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class UserLogin(APIView):
    def post(self, req):
        user = get_object_or_404(User, email=req.data["email"])
        if user.is_active == False:
            user.is_active = True
            user.save()

        refresh = RefreshToken.for_user(user)

        serializer = UserSerializer(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": serializer.data,
            }
        )
