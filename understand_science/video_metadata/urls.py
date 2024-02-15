from django.urls import path

from video_metadata.views.video_metadata import VideoMetadataView
from video_metadata.views.share_video import ShareVideoView
from video_metadata.views.category_video import CategoryVideoView

urlpatterns = [
    path("video_metadata", VideoMetadataView.as_view()),
    path("share_video", ShareVideoView.as_view()),
    path("video_by_category", CategoryVideoView.as_view()),
]
