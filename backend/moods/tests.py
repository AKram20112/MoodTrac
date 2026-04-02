"""
Tests for the moods app.
"""
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Mood

class MoodModelTest(TestCase):
    """Test cases for Mood model."""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
    
    def test_create_mood(self):
        """Test creating a mood entry."""
        mood = Mood.objects.create(
            user=self.user,
            mood='happy',
            intensity=8,
            notes='Test mood'
        )
        self.assertEqual(mood.user.username, 'testuser')
        self.assertEqual(mood.mood, 'happy')
        self.assertEqual(mood.intensity, 8)

class MoodAPITest(TestCase):
    """Test cases for Mood API."""
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.login(username='testuser', password='testpass123')
    
    def test_create_mood_api(self):
        """Test creating a mood via API."""
        data = {
            'mood': 'happy',
            'intensity': 8,
            'notes': 'Great day!'
        }
        response = self.client.post('/api/moods/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_moods_api(self):
        """Test listing moods via API."""
        response = self.client.get('/api/moods/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)