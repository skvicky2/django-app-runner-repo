from django.apps import AppConfig


class VideoMetadataConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "video_metadata"
    verbose_name = "Videos"
    
    def ready(self) -> None:
       import video_metadata.signals.share_video
