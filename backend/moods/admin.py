"""
Admin configuration for the moods app.
"""
from django.contrib import admin
from .models import Mood

@admin.register(Mood)
class MoodAdmin(admin.ModelAdmin):
    list_display = ['user', 'mood', 'intensity', 'created_at']
    list_filter = ['mood', 'created_at']
    search_fields = ['user__username', 'notes']
    readonly_fields = ['created_at', 'updated_at']