"""
Models for the moods app.
"""
from django.db import models
from django.contrib.auth.models import User

class Mood(models.Model):
    """Model to store user mood entries."""
    
    MOOD_CHOICES = [
        ('happy', 'Happy 😊'),
        ('sad', 'Sad 😢'),
        ('angry', 'Angry 😠'),
        ('anxious', 'Anxious 😰'),
        ('calm', 'Calm 😌'),
        ('excited', 'Excited 🤩'),
        ('neutral', 'Neutral 😐'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='moods')
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES)
    intensity = models.IntegerField(choices=[(i, i) for i in range(1, 11)])  # 1-10 scale
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Moods'
    
    def __str__(self):
        return f"{self.user.username} - {self.mood} ({self.created_at.date()})"