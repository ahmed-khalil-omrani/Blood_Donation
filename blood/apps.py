from django.apps import AppConfig


class bloodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blood'
    def ready(self):
        import blood
