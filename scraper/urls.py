"""
Scraper URL Configuration

The `urlpatterns` list routes URLs to views
"""
from django.urls import path
from . import views

urlpatterns = [
    path("context", views.context, name="context"),
]
