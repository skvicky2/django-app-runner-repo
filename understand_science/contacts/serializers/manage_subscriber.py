from rest_framework import serializers
from contacts.models import Subscriber

class SubscriberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subscriber
        fields = "__all__"
        read_only_fields = ('created_date',)
