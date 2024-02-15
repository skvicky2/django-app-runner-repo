from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Author(models.Model):
    """
    Stores Authors
    """

    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )
    
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text ="Scientist"
    )
    
    email = models.EmailField(max_length=255,blank=False)

    education = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    
    city = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    
    experience = models.IntegerField(blank=False, null=False, help_text ="In years")

    description = models.TextField(blank=False, null=False, verbose_name="Description")
    
    profile_picture = models.ImageField(upload_to='author_profile_picture/%Y/%m/%d/', verbose_name="Profile Picture", help_text="Author headshot picture")

    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Manage Author"
        verbose_name = "Author"
