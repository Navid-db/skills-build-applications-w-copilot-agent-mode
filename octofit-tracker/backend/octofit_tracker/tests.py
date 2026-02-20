from django.test import TestCase
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_user_create(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=team.name)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.team, 'Test Team')

    def test_activity_create(self):
        user = User.objects.create_user(username='testuser2', email='test2@example.com', password='testpass', team='Test Team')
        activity = Activity.objects.create(user=user.username, type='run', duration=30)
        self.assertEqual(activity.type, 'run')

    def test_workout_create(self):
        workout = Workout.objects.create(name='Test Workout', description='desc')
        self.assertEqual(workout.name, 'Test Workout')

    def test_leaderboard_create(self):
        user = User.objects.create_user(username='testuser3', email='test3@example.com', password='testpass', team='Test Team')
        leaderboard = Leaderboard.objects.create(user=user.username, points=100)
        self.assertEqual(leaderboard.points, 100)
