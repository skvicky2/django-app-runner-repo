from django.urls import path

from video_metadata.views.video_metadata import VideoMetadataView

urlpatterns = [
    path("video_metadata", VideoMetadataView.as_view()),
]
