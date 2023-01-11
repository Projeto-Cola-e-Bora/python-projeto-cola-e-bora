from rest_framework import serializers
from .models import Ong
from users.models import User
from rest_framework.validators import UniqueValidator


class OngSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ong
        exclude = ["users"]
        read_only_fields = [
            "id",
            "createdAt",
            "updatedAt",
            "user",
        ]
        extra_kwargs = {
            "balance": {
                "write_only": True,
            }
        }


class OngSerializerToAdm(serializers.ModelSerializer):
    class Meta:
        model = Ong
        exclude = ["users"]
        read_only_fields = [
            "id",
            "createdAt",
            "updatedAt",
            "user",
            "balance",
            "category",
        ]
