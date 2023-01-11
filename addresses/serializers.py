from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Address
from ongs.serializers import OngSerializer
import ipdb


class AddressSerializer(serializers.Serializer):
    street = serializers.CharField(max_length=127)
    number = serializers.CharField(max_length=10)
    cep = serializers.CharField(max_length=10)
    extra = serializers.CharField(max_length=100)
    id = serializers.UUIDField(read_only=True)
