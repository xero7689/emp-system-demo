"""
URL configuration for initium_interview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("portal/", include('hr_system.urls')),
    path("admin/", admin.site.urls),
]
