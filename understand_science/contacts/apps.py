from django.apps import AppConfig


class ContactsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contacts'

    def ready(self) -> None:
       import contacts.signals.manage_contact_us
       import contacts.signals.manage_subscriber