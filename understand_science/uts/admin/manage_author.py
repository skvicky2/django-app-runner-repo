from uts.models import Author
from django.contrib import admin


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "education",
        "city",
        "experience",
        "description",
        "created_by",
        "created_date",
        "updated_date",
    )

    exclude = (
        "created_by",
        "created_date",
    )
    
    search_fields = ["name", "email", "education", "city", "experience", "description"]


    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)