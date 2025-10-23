from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Limpar coleções diretamente via PyMongo para evitar problemas Djongo
        mongo_uri = getattr(settings, 'MONGO_URI', 'mongodb://localhost:27017')
        mongo_db = getattr(settings, 'MONGO_DB_NAME', 'octofit_db')
        client = MongoClient(mongo_uri)
        db = client[mongo_db]
        db.user.delete_many({})
        db.team.delete_many({})
        db.activity.delete_many({})
        db.workout.delete_many({})
        db.leaderboard.delete_many({})

        # Criar times
        marvel = Team.objects.create(name='Marvel', description='Time dos heróis Marvel')
        dc = Team.objects.create(name='DC', description='Time dos heróis DC')

        # Criar usuários
        users = []
        users.append(User.objects.create(name='Homem-Aranha', email='spiderman@marvel.com', team=marvel, is_superhero=True))
        users.append(User.objects.create(name='Capitão América', email='cap@marvel.com', team=marvel, is_superhero=True))
        users.append(User.objects.create(name='Homem de Ferro', email='ironman@marvel.com', team=marvel, is_superhero=True))
        users.append(User.objects.create(name='Mulher-Maravilha', email='wonderwoman@dc.com', team=dc, is_superhero=True))
        users.append(User.objects.create(name='Superman', email='superman@dc.com', team=dc, is_superhero=True))
        users.append(User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True))

        # Criar atividades
        Activity.objects.create(user=users[0], type='Corrida', duration=30, date='2025-10-01')
        Activity.objects.create(user=users[1], type='Natação', duration=45, date='2025-10-02')
        Activity.objects.create(user=users[3], type='Ciclismo', duration=60, date='2025-10-03')

        # Criar workouts
        w1 = Workout.objects.create(name='Treino Marvel', description='Treino para heróis Marvel')
        w1.suggested_for.add(marvel)
        w2 = Workout.objects.create(name='Treino DC', description='Treino para heróis DC')
        w2.suggested_for.add(dc)

        # Criar leaderboards
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=120)

        # Garantir índice único em email
        db.user.create_index('email', unique=True)
        self.stdout.write(self.style.SUCCESS('Banco populado com dados de exemplo!'))