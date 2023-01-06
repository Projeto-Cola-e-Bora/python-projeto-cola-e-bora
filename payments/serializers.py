from rest_framework import serializers
from .models import PaymentInfo
from rest_framework.response import Response
from rest_framework.views import status, exception_handler


class PaymentInfoSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField(method_name='get_user_id')

    def get_user_id(self, obj: PaymentInfo) -> str:
        return obj.user.id

    class Meta:
        model = PaymentInfo
        fields = ['id', 'number', 'security_code', 'due_date', 'user_id']

class UpdatePaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInfo
        fields = '__all__'
        read_only_fields = [
            'id',
            'user',
        ]