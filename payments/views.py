from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, GenericAPIView, CreateAPIView
from rest_framework.response import Response
from django.db import IntegrityError
from rest_framework.views import status, exception_handler
from django.shortcuts import get_object_or_404
from events.errors import ValidationDateError
from datetime import datetime

from .models import PaymentInfo
from .serializers import PaymentInfoSerializer, UpdatePaymentInfoSerializer, PaymentInfoErrorSerializer
from users.models import User

class PaymentView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = PaymentInfo.objects.all()
    serializer_class = PaymentInfoSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.get(id=self.kwargs['user_id'])
        payment = PaymentInfo.objects.filter(user= user)

        if not payment:
            present = datetime.now()
            date_str_list = self.request.data['due_date'].split('-')
            due_date = datetime(int(date_str_list[0]), int(date_str_list[1]), int(date_str_list[2]),)
            if present < due_date:
                return super().post(request, *args, **kwargs)

            return Response(data={'message': 'Payment method expired'}, status= status.HTTP_400_BAD_REQUEST)

        return Response(data= {'message': 'User already has a registered payment method'}, status= status.HTTP_403_FORBIDDEN)

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
