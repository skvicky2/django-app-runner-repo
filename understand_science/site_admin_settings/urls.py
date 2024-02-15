from django.urls import path
from site_admin_settings.views.manage_menu import MenuView

urlpatterns = [
    path("menu", MenuView.as_view()),
]
