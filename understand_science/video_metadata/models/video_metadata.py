from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from uts.models import Author, Tag, Category
from django.urls import reverse
from django.utils.html import format_html


class VideoMetadata(models.Model):
    """
    Stores Video Metadata
    """

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )

    description = models.TextField(blank=False, null=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    tags = models.ManyToManyField(Tag)

    video = models.FileField(upload_to="uploads/%Y/%m/%d/")
    
    poster_image = models.ImageField(upload_to='video_poster_image/%Y/%m/%d/', verbose_name="Poster Image", help_text="Video thumbnail image")
    
    citations = models.TextField(blank=False, null=False)
    
    trending = models.BooleanField(default=False)
    
    views = models.IntegerField(blank=False, null=False, default=0)
    
    likes = models.IntegerField(blank=False, null=False, default=0)
    
    shares = models.IntegerField(blank=False, null=False, default=0)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
    
    def get_tags(self):
        rel_list = "<ul>"
        for tag in self.tags.all():
            link = reverse("admin:uts_tag_change", args=[tag.id])
            rel_list += "<li><a href='%s'>%s</a></li>" % (link, tag.title)
        rel_list += "</ul>"
        return format_html(rel_list)
    
    class Meta:
        verbose_name_plural = "Videos"
        verbose_name = "Video"


   
class Qna(models.Model):
    """
    Stores Q&A of the videos
    """
    qna_video = models.ForeignKey(VideoMetadata, on_delete=models.CASCADE)
    question = models.TextField(blank=False, null=False)
    answer = models.TextField(blank=False, null=False)
    start_time = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        verbose_name="Start Time (MM.SS)"
    )