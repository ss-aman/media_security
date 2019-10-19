from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MediaSecurityConfig(AppConfig):
    name = 'media_security'
    verbose_name = _('Media Security App')

    def ready(self):
        import media_security.signals
