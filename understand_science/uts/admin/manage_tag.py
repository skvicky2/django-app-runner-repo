from uts.models import Tag
from django.contrib import admin


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "parent_tag",
        "created_by",
        "created_date",
        "updated_date",
    )

    exclude = (
        "created_by",
        "created_date",
    )
    
    search_fields = ["title", "description"]


    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)
