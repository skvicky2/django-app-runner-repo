from contacts.models import ContactUs
from django.contrib import admin
from utils.export_csv import export_as_csv


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "email",
        "message",
        "created_date",
        "updated_date",
    )

    exclude = (
        "created_date",
    )
    
    search_fields = ["first_name", "last_name", "email", "message"]
    actions = ["export_contact_us"]
    
    def export_contact_us(self, request, queryset):
        return export_as_csv(self, request, queryset, "contact_us")

    export_contact_us.short_description = "Export Selected as CSV"