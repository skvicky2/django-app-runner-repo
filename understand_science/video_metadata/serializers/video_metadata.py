from rest_framework import serializers
from video_metadata.models import VideoMetadata
from uts.models import Category, Author, Tag
from site_admin_settings.models import Menu



class CategorySerializer(serializers.ModelSerializer):
    
    menu = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ["title", "description", "menu", "created_by", "created_date", "updated_date"]
        
    def get_menu(self, obj):
        main_menu = Menu.objects.filter(sub_menu=obj.id).first()
        if main_menu:
            return main_menu.menu
        return ""
    
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
