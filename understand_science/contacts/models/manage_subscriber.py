from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    """
    Stores Subscribers
    """
    
    email = models.EmailField(max_length=255,blank=False, null=False, unique=True,)
    
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name_plural = "Manage Subscribers"
        verbose_name = "Subscriber"
