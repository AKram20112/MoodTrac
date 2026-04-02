"""
URL configuration for moodtrac project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from moods.views import MoodViewSet, UserMoodStatsView

router = DefaultRouter()
router.register(r'moods', MoodViewSet, basename='mood')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/stats/', UserMoodStatsView.as_view(), name='mood-stats'),
    path('api-auth/', include('rest_framework.urls')),
]