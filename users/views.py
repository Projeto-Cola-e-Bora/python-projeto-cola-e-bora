from rest_framework import generics
from .models import User
from .serializers import UserSerializer, LoginSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserOwner
from rest_framework.views import APIView, Response, status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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
        data_serializer = LoginSerializer(data=req.data)
        data_serializer.is_valid(raise_exception=True)

        try:
            user = get_object_or_404(User, email=req.data["email"])
        except:
            return Response({"detail": "No active account found with the given credentials"}, status.HTTP_403_FORBIDDEN)

        if user.is_active == False:
            user.is_active = True
            user.save()

        login_serializer = TokenObtainPairSerializer(data=req.data)
        login_serializer.is_valid(raise_exception=True)

        refresh = RefreshToken.for_user(user)

        user_serializer = UserSerializer(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": user_serializer.data,
            }
        )
