from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Tag(models.Model):
    """
    Stores Tags
    """

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )

    description = models.TextField(blank=False, null=False, verbose_name="Description")
    
    parent_tag = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Parent Tag",  blank=True, null=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Manage Tag"
        verbose_name = "Tag"
