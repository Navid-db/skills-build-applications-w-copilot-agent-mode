from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (superheroes)
        ironman = User.objects.create_user(
            username='ironman',
            email='ironman@marvel.com',
            password='avengers123',
            first_name='Tony',
            last_name='Stark',
            team='Marvel'
        )
        captain = User.objects.create_user(
            username='captainamerica',
            email='captain@marvel.com',
            password='avengers123',
            first_name='Steve',
            last_name='Rogers',
            team='Marvel'
        )
        thor = User.objects.create_user(
            username='thor',
            email='thor@marvel.com',
            password='avengers123',
            first_name='Thor',
            last_name='Odinson',
            team='Marvel'
        )
        batman = User.objects.create_user(
            username='batman',
            email='batman@dc.com',
            password='justice123',
            first_name='Bruce',
            last_name='Wayne',
            team='DC'
        )
        superman = User.objects.create_user(
            username='superman',
            email='superman@dc.com',
            password='justice123',
            first_name='Clark',
            last_name='Kent',
            team='DC'
        )
        wonderwoman = User.objects.create_user(
            username='wonderwoman',
            email='wonderwoman@dc.com',
            password='justice123',
            first_name='Diana',
            last_name='Prince',
            team='DC'
        )

        # Create activities
        Activity.objects.create(user='ironman', type='run', duration=30)
        Activity.objects.create(user='ironman', type='cycle', duration=45)
        Activity.objects.create(user='captainamerica', type='run', duration=60)
        Activity.objects.create(user='thor', type='weightlifting', duration=90)
        Activity.objects.create(user='batman', type='run', duration=50)
        Activity.objects.create(user='batman', type='martial_arts', duration=120)
        Activity.objects.create(user='superman', type='fly', duration=30)
        Activity.objects.create(user='wonderwoman', type='combat', duration=75)

        # Create workouts
        Workout.objects.create(
            name='Hero HIIT',
            description='High intensity interval training designed for superheroes'
        )
        Workout.objects.create(
            name='Power Yoga',
            description='Yoga routine to enhance super strength and flexibility'
        )
        Workout.objects.create(
            name='Avengers Bootcamp',
            description='Full body workout inspired by Marvel heroes'
        )
        Workout.objects.create(
            name='Justice League Training',
            description='Comprehensive training program from the DC universe'
        )

        # Create leaderboard
        Leaderboard.objects.create(user='ironman', points=150)
        Leaderboard.objects.create(user='batman', points=180)
        Leaderboard.objects.create(user='superman', points=200)
        Leaderboard.objects.create(user='captainamerica', points=140)
        Leaderboard.objects.create(user='wonderwoman', points=175)
        Leaderboard.objects.create(user='thor', points=160)

        self.stdout.write(self.style.SUCCESS('Successfully populated octofit_db with superhero test data!'))
