
from rest_framework.response import Response
from rest_framework import status
from video_metadata.models import VideoMetadata
from video_metadata.serializers import VideoMetadataSerializer
from rest_framework import generics

class VideoMetadataView(generics.CreateAPIView):
    queryset = VideoMetadata.objects.all()
    serializer_class = VideoMetadataSerializer
    http_method_names = ["get", "put"]
    
    def get(self, request, *args, **kwargs):
        """
        List all the videos
        """
        videos = VideoMetadata.objects.all()
        serializer = VideoMetadataSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        try:
            id_value =  request.data['id']
            action_value =  request.data['action']
            if id_value != None and action_value != None:
                video = VideoMetadata.objects.get(id=id_value)
                setattr(video, action_value, getattr(video, action_value) + 1)
                video.save()
                serializer = VideoMetadataSerializer(video)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(data="Invalid request data", status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(data="Invalid request data", status=status.HTTP_400_BAD_REQUEST)
        