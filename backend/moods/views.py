"""
Views for the moods app.
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Avg
from .models import Mood
from .serializers import MoodSerializer

class MoodViewSet(viewsets.ModelViewSet):
    """ViewSet for Mood model."""
    serializer_class = MoodSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Return moods for the current user."""
        return Mood.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """Create a mood entry for the current user."""
        serializer.save(user=self.request.user)
    
    @action(detail=False, methods=['get'])
    def today(self, request):
        """Get today's mood entries."""
        from datetime import date
        today_moods = self.get_queryset().filter(created_at__date=date.today())
        serializer = self.get_serializer(today_moods, many=True)
        return Response(serializer.data)

class UserMoodStatsView(APIView):
    """View for mood statistics."""
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        """Get mood statistics for the current user."""
        moods = Mood.objects.filter(user=request.user)
        
        # Most common mood
        most_common_mood = moods.values('mood').annotate(count=Count('mood')).order_by('-count').first()
        
        # Average intensity
        avg_intensity = moods.aggregate(Avg('intensity'))['intensity__avg']
        
        # Total entries
        total_entries = moods.count()
        
        return Response({
            'total_entries': total_entries,
            'most_common_mood': most_common_mood['mood'] if most_common_mood else None,
            'average_intensity': round(avg_intensity, 2) if avg_intensity else 0,
        })
