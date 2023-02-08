from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'full_name', 
            'email',
            'password', 
            'phone',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    email = serializers.EmailField(validators = [
        UniqueValidator(
            queryset=User.objects.all(),
            message='This field must be unique.'
        )]
    )

    username = serializers.CharField(validators = [
        UniqueValidator(
            queryset=User.objects.all(),
            message='This field must be unique.'
        )]
    )

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
    

def update(self, instance: User, validated_data: dict) -> User:
    for key, value in validated_data.items():
        if key == "password":
            value = make_password(value)
        setattr(instance, key, value)

    instance.save()

    return instance