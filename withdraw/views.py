from rest_framework import generics
from .models import Withdraw
from ongs.models import Ong
from .serializers import WithdrawSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsUserOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response, status


class WithdrawView(generics.ListCreateAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserOwner]


    def create(self, request, pk):
        user = request.user
        ong = Ong.objects.get(pk=pk)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, user, ong)
        result_ong_balance = self.updateOngBalance(serializer.data["value"], ong)
        if result_ong_balance == "insufficient funds":
            return Response({"detail": "Insufficient funds"}, status=status.HTTP_401_UNAUTHORIZED
        )
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer, user, ong):
        return serializer.save(user=user, ong=ong)

    def updateOngBalance(self, value, ong: Ong):
        new_balance = float(ong.balance) - float(value)
        if new_balance < 0:
            return ("insufficient funds")
        ong.balance = new_balance
        ong.save()

    
    def get(self, request, pk):
        user = request.user
        ong = Ong.objects.get(pk=pk)
        if ong.user.id != user.id:
            return Response(
                {"detail": "Not authorizated"}, status=status.HTTP_401_UNAUTHORIZED
            )

        withdraw = Withdraw.objects.filter(ong=ong)
        serializer = self.get_serializer(withdraw, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
