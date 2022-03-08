"""
Apps configuration for the dictionary app in the flashcards project enabling configuration of AppConfig subclass
"""
from django.apps import AppConfig


class InputManipulationConfig(AppConfig):
    """
    Return a subclass of AppConfig to configure the app
    BigAutoField is a 64-bit integer
    :param AppConfig: a subclass of AppConfig that configures the given app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'input_manipulation'
