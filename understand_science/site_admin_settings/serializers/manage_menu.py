from rest_framework import serializers
from site_admin_settings.models import Menu
from uts.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
        
class MenuSerializer(serializers.ModelSerializer):
    
    sub_menu = CategorySerializer(many=True)
    
    class Meta:
        model = Menu
        fields = "__all__"