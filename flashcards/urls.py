"""flashcards URL Configuration

The `urlpatterns` list routes URLs to views
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dictionary.urls')),
    path('', include('input_manipulation.urls')),
    path('', include('static_page.urls')),
    path('', include('scraper.urls')),
]
