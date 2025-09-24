"""URL configuration for the stream app."""
from __future__ import annotations

from django.urls import path

from . import views

app_name = "stream"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
