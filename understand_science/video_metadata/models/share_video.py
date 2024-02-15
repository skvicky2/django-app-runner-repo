from django.db import models
from django.utils import timezone
from video_metadata.models import VideoMetadata

class ShareVideo(models.Model):
    """
    Stores shared videos
    """
    video = models.ForeignKey(VideoMetadata, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255,blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.email)
    
    class Meta:
        verbose_name_plural = "Manage Share Video"
        verbose_name = "Share Video"
