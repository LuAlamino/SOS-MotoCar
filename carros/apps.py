from django.apps import AppConfig


class CarrosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carros'

    def ready(self):
        import carros.signals

