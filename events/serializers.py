from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from addresses.models import Address
from events.models import Event
from addresses.serializers import AddressSerializer
from ongs.serializers import OngSerializer
from django.core.exceptions import ValidationError
import datetime

from django.forms.models import model_to_dict


class EventSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=127)
    description = serializers.CharField()
    date = serializers.DateTimeField()
    address = AddressSerializer()
    ong = serializers.SerializerMethodField(read_only=True)
    id = serializers.UUIDField(read_only=True)

    def create(self, validated_data: dict) -> Event:
        # if self.date < datetime.date.today():
        #     raise ValidationError("The date cannot be in the past!")

        address_dict = validated_data.pop("address")
        address_obj, address_created = Address.objects.get_or_create(**address_dict)

        event = Event.objects.create(**validated_data, address=address_obj)
        return event

    def update(self, instance, validated_data):
        address_dict = validated_data.pop("address", None)

        if address_dict:
            address_obj, created = Address.objects.get_or_create(**address_dict)
            for key, value in address_dict.items():
                setattr(address_obj, key, value)
            address_obj.save()
            instance.address = address_obj

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    def get_ong(self, obj):
        return dict({"id": obj.ong.id, "name": obj.ong.name, "email": obj.ong.email})
