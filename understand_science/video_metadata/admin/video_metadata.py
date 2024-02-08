from video_metadata.models import VideoMetadata, Qna
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.db import models
from django.forms import Textarea




class QnaInline(admin.TabularInline):
    model = Qna
    verbose_name="Question & Answer"
    verbose_name_plural = "Associated Question & Answer"
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                       attrs={'rows': 3,
                              'cols': 40})},
}
    
    
@admin.register(VideoMetadata)
class VideoMetadataAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "category_name",
        "author_name",
        "get_tags",
        "trending",
        "views",
        "likes",
        "shares",
        "created_by",
        "created_date",
        "updated_date",
    )
    exclude = (
        "views",
        "likes",
        "shares",
        "created_by",
        "created_date",
    )
    inlines = (QnaInline,)
  
    
    search_fields = ["description", "category__title", "author__name", "tags__title"]
    
    def author_name(self, obj):
        link = reverse("admin:uts_author_change", args=[obj.author.id])
        return format_html('<a href="{}">{}</a>', link, obj.author.name)
    
    def category_name(self, obj):
        link = reverse("admin:uts_category_change", args=[obj.category.id])
        return format_html('<a href="{}">{}</a>', link, obj.category.title)
    
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
