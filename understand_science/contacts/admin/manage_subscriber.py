from contacts.models import Subscriber
from django.contrib import admin
from utils.export_csv import export_as_csv


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "created_date",
        "updated_date",
    )

    exclude = (
        "created_date",
    )
    
    search_fields = ["email"]
    actions = ["export_subscriber"]
    
    def export_subscriber(self, request, queryset):
        return export_as_csv(self, request, queryset, "subscribers")

    export_subscriber.short_description = "Export Selected as CSV"