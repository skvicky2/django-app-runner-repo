from django.db import models
from django.utils import timezone
from video_metadata.models import VideoMetadata

class ShareVideo(models.Model):
    """
    Stores shared videos
    """
    video = models.ForeignKey(VideoMetadata, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255,blank=False, verbose_name="To Email")
    to_name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="To Name",
        default=""
    )
    from_email = models.EmailField(max_length=255,blank=False, verbose_name="From Email", default="")
    from_name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name="From Name",
        default=""
    )
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.email)
    
    class Meta:
        verbose_name_plural = "Shared Videos"
        verbose_name = "Shared Video"
