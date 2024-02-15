from video_metadata.models import ShareVideo
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

    
@admin.register(ShareVideo)
class ShareVideoAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "video_title",
        "created_date",
        "updated_date",
    )
    exclude = (
        "created_date",
        "updated_date",
    )
    
    search_fields = ["email", "video__title"]
    
    def video_title(self, obj):
        link = reverse("admin:video_metadata_videometadata_change", args=[obj.video.id])
        return format_html('<a href="{}">{}</a>', link, obj.video.title)
    
    