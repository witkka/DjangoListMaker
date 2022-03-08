"""
Configuration for the 'scraper' app.
"""
from django.apps import AppConfig


class ScraperConfig(AppConfig):
    """
        Return a subclass of AppConfig to configure the app
        BigAutoField is a 64-bit integer
        :param AppConfig: a subclass of AppConfig that configures the given app
        """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scraper'
