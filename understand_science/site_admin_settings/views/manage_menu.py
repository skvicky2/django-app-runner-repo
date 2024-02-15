from rest_framework.response import Response
from rest_framework import status
from site_admin_settings.models import Menu
from site_admin_settings.serializers import MenuSerializer
from rest_framework import generics

class MenuView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
    def get(self, request, *args, **kwargs):
        """
        List all the menu and submenus
        """
        contact_us = Menu.objects.all()
        serializer = MenuSerializer(contact_us, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
