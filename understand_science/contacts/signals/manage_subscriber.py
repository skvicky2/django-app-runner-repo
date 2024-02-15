from django.db.models.signals import post_save
from django.dispatch import receiver
from contacts.models import Subscriber
from utils.email_config import trigger_email

@receiver(post_save, sender=Subscriber)
def subscriber_post_save(sender, instance, created, **kwargs):
    """
    Send mail to the Subscriber
    """
    if created:
        try:
            # Send the video url and video title in email 
            subject="Video Understand The Science"
            recipient_list=[instance.email]
            text_content=""
            html_content= """
            <p>Hello,</p>
 
            <p style="margin-top: 1em">
               Thanks for subscribing us. Our team will get back to you soon.
            </p>
            
            <p style="margin-top: 1em">
                Our mission is to provide easy-to-understand medical education on crucial healthcare topics to empower informed health decisions.
            </p>
            
            <p style="margin-top: 1em"><em>Stay tuned for more updates from us!</em></p>
 
            <p style="margin-top: 1em">Regards,</p>
            <p style="margin-top: 0.2em !important;">Understand The Science Dev Team</p>`,
            """

            trigger_email(subject, recipient_list, text_content, html_content)

        except Exception as e:
            print('There was an error sending an email to {instance.email}: ', e) 
        
        
        


