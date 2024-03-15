from django.db import models
from django.utils import timezone


class ContactUs(models.Model):
    """
    Stores Contact Us details
    """

    first_name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    
    last_name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    
    email = models.EmailField(max_length=255,blank=False)

    message = models.TextField(blank=False, null=False, verbose_name="Your Message")
    
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.first_name)

    class Meta:
        verbose_name_plural = "Contact Us"
        verbose_name = "Contact Us"
