from django.db.models.signals import post_save
from django.dispatch import receiver
from video_metadata.models import ShareVideo, VideoMetadata
from utils.email_config import trigger_email

@receiver(post_save, sender=ShareVideo)
def share_video_post_save(sender, instance, created, **kwargs):
    """
    Update the shares count in the video metadata and trigger mail
    """
    if created:
        video = VideoMetadata.objects.get(id=instance.video_id)
        video.shares = video.shares + 1
        video.save()
        
        try:
            # Send the video url and video title in email 
            subject="Video Understand The Science"
            recipient_list=[instance.email]
            text_content=""
            html_content= """
            <p>Hello,</p>
 
            <p style="margin-top: 1em">
                Shared Video Title - <b>{}</b> and Shared Video URL - <b>{}</b>
            </p>
            
            <p style="margin-top: 1em">
                Our mission is to provide easy-to-understand medical education on crucial healthcare topics to empower informed health decisions.
            </p>
            
            <p style="margin-top: 1em"><em>Stay tuned for more updates from us!</em></p>
 
            <p style="margin-top: 1em">Regards,</p>
            <p style="margin-top: 0.2em !important;">Understand The Science Dev Team</p>`,
            """.format(video.title, video.video)

            trigger_email(subject, recipient_list, text_content, html_content)

        except Exception as e:
            print('There was an error sending an email to {instance.email}: ', e) 
        
        
        


