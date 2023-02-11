from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id', 
            'full_name', 
            'email', 
            'phone',
            'created_at',
            'users_id'
        ]