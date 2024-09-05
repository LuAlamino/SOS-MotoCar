from django.apps import AppConfig


class MecanicoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Mecanico'

    def ready(self):
        import Mecanico.signals
