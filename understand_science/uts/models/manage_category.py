from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Stores Categorys
    """

    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )

    description = models.TextField(blank=False, null=False, verbose_name="Description")

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = "Manage Category"
        verbose_name = "Category"
