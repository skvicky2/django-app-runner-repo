# Import necessary modules
from django.core.mail import EmailMultiAlternatives

def trigger_email(subject, recipient_list, text_content, html_content):
    """
    Function to send an email.
    """
    msg = EmailMultiAlternatives(subject, text_content, None, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()




