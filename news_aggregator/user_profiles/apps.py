from django.apps import AppConfig


class UserProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_profiles'

    def ready(self) -> None:
        from . signals import sync_profile
        return super().ready()