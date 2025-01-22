from django.core.management.base import BaseCommand
from ...models import User

class Command(BaseCommand):
    help = 'Seeds the database with two users'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='ricky').exists():
            ricky = User.objects.create(
                username='ricky',
                password='SunnyvaleKing2025',
            )
            self.stdout.write(self.style.SUCCESS('Successfully created ricky!'))

        if not User.objects.filter(username='bubbles').exists():
            bubbles = User.objects.create(
                username='bubbles',
                password='KittyLord99',
            )
            self.stdout.write(self.style.SUCCESS('Successfully created bubbles!'))