"""
URL configuration for app project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# views
from people.views import Diretoria
from documents.views import iframe_documents_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("diretoria/", Diretoria.as_view()),
    path("documentos/", iframe_documents_view),
    path("", include("home_page.urls")),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
