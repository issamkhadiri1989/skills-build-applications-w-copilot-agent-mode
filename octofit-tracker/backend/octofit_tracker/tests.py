from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(str(user), 'testuser')

    def test_create_activity(self):
        activity = Activity.objects.create(user='testuser', type='Running', duration=30, team='Test Team')
        self.assertEqual(str(activity), 'testuser - Running')

    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(str(leaderboard), 'Test Team: 100')

    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', suggested_for='Test Team')
        self.assertEqual(str(workout), 'Test Workout')
