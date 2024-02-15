from rest_framework.response import Response
from rest_framework import status
from video_metadata.models import VideoMetadata
from video_metadata.serializers import VideoMetadataSerializer
from rest_framework import generics

class CategoryVideoView(generics.CreateAPIView):
    
    queryset = VideoMetadata.objects.all()
    serializer_class = VideoMetadataSerializer
    
    def get(self, request, *args, **kwargs):
        """
        List all the videos mapped to the given category ID
        """
        try:
            cat_id = request.query_params['id']
            contact_us = VideoMetadata.objects.filter(category_id=cat_id)
            serializer = VideoMetadataSerializer(contact_us, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
           return Response([], status=status.HTTP_200_OK)
