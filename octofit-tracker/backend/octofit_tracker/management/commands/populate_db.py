from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connection

from djongo import models

# Define models if not already defined elsewhere
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password')
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password')

        # Create activities
        Activity.objects.create(user='ironman', type='Running', duration=30, team='Marvel')
        Activity.objects.create(user='batman', type='Cycling', duration=45, team='DC')
        Activity.objects.create(user='spiderman', type='Swimming', duration=25, team='Marvel')
        Activity.objects.create(user='superman', type='Flying', duration=60, team='DC')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=55)
        Leaderboard.objects.create(team='DC', points=105)

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes', suggested_for='Marvel')
        Workout.objects.create(name='Power Lift', description='Strength training for super strength', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
