"""
input_manipulation URL Configuration

The `urlpatterns` list routes URLs to views
"""
from django.urls import path
from . import views

urlpatterns = [
    path('new', views.new, name='new'),

]
