from rest_framework.response import Response
from rest_framework import status
from video_metadata.models import ShareVideo
from video_metadata.serializers import ShareVideoSerializer
from rest_framework import generics

class ShareVideoView(generics.CreateAPIView):
    queryset = ShareVideo.objects.all()
    serializer_class = ShareVideoSerializer
    
    def get(self, request, *args, **kwargs):
        """
        List all the shared videos
        """
        contact_us = ShareVideo.objects.all()
        serializer = ShareVideoSerializer(contact_us, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
