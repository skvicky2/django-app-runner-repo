# Import necessary modules
from django.core.mail import send_mail
from django.conf import settings

def trigger_email(subject, text_content, recipient_list, html_content):
    """
    Function to send an email.
    """
    send_mail(subject, text_content, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False, html_message=html_content)
