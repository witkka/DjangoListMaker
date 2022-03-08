"""
Dictionary URL Configuration
The `urlpatterns` list routes URLs to views.
"""
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("list", views.word_list_page, name="list"),
    path("word_check", views.check_word_form, name="check"),
    re_path(r"download", views.download_list, name="download"),
]
