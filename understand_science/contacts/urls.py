from django.urls import path

from contacts.views.manage_contact_us import ContactUsView
from contacts.views.manage_subscriber import SubscriberView

urlpatterns = [
    path("contact_us", ContactUsView.as_view()),
    path("subscriber", SubscriberView.as_view()),
]
