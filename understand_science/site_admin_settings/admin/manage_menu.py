from site_admin_settings.models import Menu
from django.contrib import admin


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        "menu",
        "get_sub_menu",
        "created_date",
        "updated_date",
    )

    exclude = (
        "created_date",
    )
    
    search_fields = ["menu", "sub_menu__title"]