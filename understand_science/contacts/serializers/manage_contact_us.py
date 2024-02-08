from rest_framework import serializers
from contacts.models import ContactUs

class ContactUsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContactUs
        fields = "__all__"
        read_only_fields = ('created_date',)
