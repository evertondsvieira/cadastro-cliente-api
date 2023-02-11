from .models import Contact
from .serializers import ContactSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

class ContactView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    
    def perform_create(self, serializer):
        print(self.request)
        serializer.save(users=self.request.user)

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = ContactSerializer
    queryset = Contact.objects.all()