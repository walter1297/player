from __future__ import annotations

from django.apps import AppConfig


class StreamConfig(AppConfig):
    """Default configuration for the stream app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "stream"
    verbose_name = "磁链播放器"
