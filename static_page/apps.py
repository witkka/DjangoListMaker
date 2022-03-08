"""
Configuration for the 'static_page' app.
"""
from django.apps import AppConfig


class StaticPageConfig(AppConfig):
    """
        Return a subclass of AppConfig to configure the app
        BigAutoField is a 64-bit integer
        :param AppConfig: a subclass of AppConfig that configures the given app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'static_page'
