from rest_framework.response import Response
from rest_framework import status
from contacts.models import Subscriber
from contacts.serializers import SubscriberSerializer
from rest_framework import generics

class SubscriberView(generics.CreateAPIView):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    
    def get(self, request, *args, **kwargs):
        """
        List all the subscriber details
        """
        subscriber = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscriber, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
