from django.core.management.base import BaseCommand
from ...models import User

class Command(BaseCommand):
    help = 'Seeds the database with two users'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='user1').exists():
            user1 = User.objects.create(
                username='user1',
                password='password1',
            )
            self.stdout.write(self.style.SUCCESS('Successfully created user1'))

        if not User.objects.filter(username='user2').exists():
            user2 = User.objects.create(
                username='user2',
                password='password2',
            )
            self.stdout.write(self.style.SUCCESS('Successfully created user2'))