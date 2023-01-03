from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    name = serializers.CharField()


    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)


    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "birth_date" or key == "name" or key == "email":
                setattr(instance, key, value)
            elif key == "password":
                instance.set_password(value)

        instance.save()

        return instance


    class Meta:
            model = User
            fields = ['id', 'name', 'email', "birth_date", 
                    'password', "create_at", "update_at", 'is_superuser', "is_active"]
            extra_kwargs = {"password": {"write_only": True}}