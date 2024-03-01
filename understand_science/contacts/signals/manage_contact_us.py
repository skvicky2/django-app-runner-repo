from django.db.models.signals import post_save
from django.dispatch import receiver
from contacts.models import ContactUs
from utils.email_config import trigger_email
from django.conf import settings

def trigger_mail_customer(email):
    # Send acknowledge mail to the customer 
    subject="Video Understand The Science"
    recipient_list= [email]
    text_content=""
    html_content= """
    <p>Hello,</p>

    <p style="margin-top: 1em">
        Thanks for contacting us. Our team will get back to you soon.
    </p>
    
    <p style="margin-top: 1em">
        Our mission is to provide easy-to-understand medical education on crucial healthcare topics to empower informed health decisions.
    </p>
    
    <p style="margin-top: 1em"><em>Stay tuned for more updates from us!</em></p>

    <p style="margin-top: 1em">Regards,</p>
    <p style="margin-top: 0.2em !important;">Understand The Science Dev Team</p>`,
    """

    trigger_email(subject, text_content, recipient_list, html_content)
    
def trigger_mail_dev_team(customer):
    # Send customer details email to the dev team
    subject="Video Understand The Science"
    recipient_list= [settings.EMAIL_HOST_USER]
    text_content=""
    html_content= f"""
    <p>Hello Team,</p>
    
    <p style="margin-top: 1em">
        The customer sent us a message. Contact information is provided below.
    </p>

    <h2>Contact Information </h2>
    <table>
        <tr>
            <td><b> First Name </b></td>
            <td>{customer.first_name}</td>
        </tr>
        <tr>
            <td><b> Last Name </b></td>
            <td>{customer.last_name}</td>
        </tr>
        <tr>
            <td><b> Email </b></td>
            <td>{customer.email}</td>
        </tr>
        <tr>
            <td><b> Message </b></td>
            <td>{customer.message}</td>
        </tr>
    </table>
    
    <p style="margin-top: 1em">
        Our mission is to provide easy-to-understand medical education on crucial healthcare topics to empower informed health decisions.
    </p>
    
    <p style="margin-top: 1em">Regards,</p>
    <p style="margin-top: 0.2em !important;">Understand The Science Dev Team</p>`,
    """

    trigger_email(subject, text_content, recipient_list, html_content)
    
@receiver(post_save, sender=ContactUs)
def contact_us_post_save(sender, instance, created, **kwargs):
    """
    Send mail to the contact person
    """
    if created:
        try:
            trigger_mail_customer(instance.email)
            trigger_mail_dev_team(instance)
        except Exception as e:
            print('There was an error sending an email to {instance.email}: ', e) 
        
        
        


