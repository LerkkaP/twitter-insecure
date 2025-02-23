from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from twitter.models import Post

class Command(BaseCommand):
    help = 'Seeds the database with two users'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='ricky').exists():
            ricky = User.objects.create_user(
                username='ricky',
                password='SunnyvaleKing2025',
            )
            self.stdout.write(self.style.SUCCESS('Successfully created ricky!'))

            ricky_posts = [
                "Math is dumb, but I’m smart enough to know that pepperoni is a vegetable. 💡",
                "Got 6 birds stoned at once today. That’s efficiency. 🐦🔥",
                "The car’s fine, Julian. It just needs a new engine, four tires, and some duct tape. 🚗",
                "Smokes. Let’s go. That’s the tweet. 🚬",
                "If you can’t spell it, it’s probably not important."
            ]
            for text in ricky_posts:
                Post.objects.create(text=text, user=ricky)

        if not User.objects.filter(username='bubbles').exists():
            bubbles = User.objects.create_user(
                username='bubbles',
                password='KittyLord99',
            )
            self.stdout.write(self.style.SUCCESS('Successfully created bubbles!'))

            bubbles_posts = [
                "Found a new kitty today. Named him Scrappy Doo. Best day ever! 🐱❤️",
                "Julian’s rum glass is like a superhero cape. He never takes it off. 🥃🦸‍♂️",
                "Kitty treats are like cat crack. The boys went nuts! 🐈💨",
                "The shed is looking mighty fine today. Fresh coat of paint, clean litter boxes. 🛠️",
                "Saw Randy without his shirt on again. My eyes are scarred. 🧀"
            ]
            for text in bubbles_posts:
                Post.objects.create(text=text, user=bubbles)