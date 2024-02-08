from rest_framework.response import Response
from rest_framework import status
from contacts.models import ContactUs
from contacts.serializers import ContactUsSerializer
from rest_framework import generics

class ContactUsView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    
    def get(self, request, *args, **kwargs):
        """
        List all the contact us details
        """
        contact_us = ContactUs.objects.all()
        serializer = ContactUsSerializer(contact_us, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
