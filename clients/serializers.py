from rest_framework import serializers
from .models import Client
from rest_framework.validators import UniqueValidator

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'email', 
            'password', 
            'full_name', 
            'phone',
        ]
        extra_kwargs = {'password': {'write_only': True}}


    email = serializers.EmailField(validators = [
        UniqueValidator(
            queryset=Client.objects.all(),
            message='This field must be unique.'
        )]
    )


    def create(self, validated_data: dict) -> Client:
        return Client.objects.create_user(**validated_data)


    def update(self, instance: Client, validated_data: dict) -> Client:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance