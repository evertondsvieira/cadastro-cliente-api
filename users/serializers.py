from rest_framework import serializers
from .models import User
from contacts.serializers import ContactSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'full_name', 
            'email',
            'password', 
            'phone',
            'created_at',
            'contacts',
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
        password = validated_data.pop('password', None)
        if password:
            validated_data['password'] = make_password(password)
        user = User.objects.create(**validated_data)
        return user
    
    
    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                value = make_password(value)
            setattr(instance, key, value)

        instance.save()

        return instance