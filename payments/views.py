from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, GenericAPIView
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework.views import status, exception_handler
from django.shortcuts import get_object_or_404

from .models import PaymentInfo
from .serializers import PaymentInfoSerializer, UpdatePaymentInfoSerializer
from users.models import User

class PaymentView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = PaymentInfo.objects.all()
    serializer_class = PaymentInfoSerializer

    def perform_create(self, serializer):
        user = User.objects.get(id=self.kwargs['user_id'])
        return serializer.save(user=user)

class PaymentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = PaymentInfo.objects.all()
    serializer_class = UpdatePaymentInfoSerializer

    def retrieve(self, request, *args, **kwargs):
        user = get_object_or_404(User.objects.all(), id=self.kwargs['user_id'])
        payment_method = get_object_or_404(PaymentInfo.objects.all(), user=user) 
        return Response(PaymentInfoSerializer(payment_method).data)

    def destroy(self, instance, pk = None, user_id = None, ):
        user = get_object_or_404(User.objects.all(), id=self.kwargs['user_id'])
        target = get_object_or_404(PaymentInfo.objects.all(), user=user)
        target.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
