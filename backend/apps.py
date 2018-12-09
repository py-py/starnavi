from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BackendConfig(AppConfig):
    name = 'backend'
    verbose_name = _('Backend')
