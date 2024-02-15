from rest_framework import serializers
from video_metadata.models import ShareVideo

class ShareVideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ShareVideo
        fields = "__all__"
        read_only_fields = ('created_date',)
