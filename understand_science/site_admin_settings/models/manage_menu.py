from django.db import models
from django.utils import timezone
from uts.models import Category
from django.urls import reverse
from django.utils.html import format_html

class Menu(models.Model):
    """
    Stores Menu and Submenu of site portal
    """

    menu = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        unique=True,
    )
    
    sub_menu = models.ManyToManyField(Category, verbose_name="Sub Menu")
    
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.menu)
    
    def get_sub_menu(self):
        rel_list = "<ul>"
        for category in self.sub_menu.all():
            link = reverse("admin:uts_category_change", args=[category.id])
            rel_list += "<li><a href='%s'>%s</a></li>" % (link, category.title)
        rel_list += "</ul>"
        return format_html(rel_list)

    class Meta:
        verbose_name_plural = "Manage Menu"
        verbose_name = "Menu"
