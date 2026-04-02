from django.urls import path, include
from rest_framework.routers import DefaultRouter
from moods.views import MoodViewSet, UserMoodStatsView

router = DefaultRouter()
router.register(r'moods', MoodViewSet, basename='mood')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/stats/', UserMoodStatsView.as_view(), name='mood-stats'),
]