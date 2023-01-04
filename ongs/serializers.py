from rest_framework import serializers
from .models import Ong


class OngSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ong
        fields = "__all__"
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
        fields = "__all__"
        read_only_fields = [
            "id",
            "createdAt",
            "updatedAt",
            "user",
            "balance",
            "category",
        ]
