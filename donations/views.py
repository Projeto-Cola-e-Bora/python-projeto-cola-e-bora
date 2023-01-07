from django.shortcuts import get_object_or_404

from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Donation
from .serializers import DonationSerializer
from .permissions import IsOwnerOrDonateOnly

from ongs.models import Ong


class DonationView(ListCreateAPIView, PageNumberPagination):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrDonateOnly]

    def get(self, request, pk, *args, **kwargs):
        user = request.user
        ong = get_object_or_404(Ong, pk=pk)
        if ong.user.id != user.id:
            return Response(
                {"detail": "Not authorizated"}, status=status.HTTP_401_UNAUTHORIZED
            )

        donations = Donation.objects.filter(ong=ong)
        serializer = self.get_serializer(donations, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, pk, *args, **kwargs):
        user = request.user
        ong = get_object_or_404(Ong, pk=pk)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, user, ong)
        self.sumOngBalance(serializer.data["value"], ong)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer, user, ong):
        return serializer.save(user=user, ong=ong)

    def sumOngBalance(self, value, ong: Ong):
        newBalance = float(ong.balance) + float(value)
        ong.balance = newBalance

        ong.save()
