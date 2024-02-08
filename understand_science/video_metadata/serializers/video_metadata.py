from rest_framework import serializers
from video_metadata.models import VideoMetadata
from uts.models import Category, Author, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
      
      
class VideoMetadataSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer()
    author = AuthorSerializer()
    tags = TagSerializer(many=True)
    
    class Meta:
        model = VideoMetadata
        fields = "__all__"
