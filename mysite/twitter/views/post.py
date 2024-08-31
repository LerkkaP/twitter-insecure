from ..models import Post, User
from django.contrib import messages
from django.utils import timezone
from django.db import connection

def add_post(request, username, text):
    if request.method == 'POST':
        text = request.POST.get('text')
        username = request.session.get('username')  # Fetch username from session
        if username:
            try:
                user_instance = User.objects.get(username=username)
                if len(text) > 280:
                    messages.error(request, "Max length 280 characters!")
                else:
                    with connection.cursor() as cursor:
                        created_at = timezone.now().date()
                        cursor.execute(f"INSERT INTO twitter_post (text, user_id, created_at) VALUES ('{text}', {user_instance.id}, '{created_at}')")
                        #cursor.execute(f"INSERT INTO POST text = '{text}' ")

                    #Post.objects.create(text=text, user=user_instance)
                    messages.success(request, "Post added successfully!")
            except User.DoesNotExist:
                messages.error(request, "User does not exist.")
        else:
            messages.error(request, "You need to be logged in to post.")