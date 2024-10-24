"""from ..models import Post, User
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
                        query = f"INSERT INTO twitter_post (text, user_id, created_at) VALUES ('{text}', {user_instance.id}, '{created_at}')"
                        print(query)
                        cursor.execute(query)
                        #cursor.execute(f"INSERT INTO POST text = '{text}' ")

                    #Post.objects.create(text=text, user=user_instance)
                    messages.success(request, "Post added successfully!")
            except User.DoesNotExist:
                messages.error(request, "User does not exist.")
        else:
            messages.error(request, "You need to be logged in to post.")"""

from ..models import Post, User, Comment
from django.contrib import messages
from django.utils import timezone
from django.db import connection

def add_post(request, username, text):
    if request.method == 'POST':
        text = request.POST.get('text')
        username = request.session.get('username') 
        if username:
            try:
                user_instance = User.objects.get(username=username)
                if len(text) > 280:
                    messages.error(request, "Max length 280 characters!")
                else:
                    created_at = timezone.now().strftime('%Y-%m-%d') 
                    query = f"INSERT INTO twitter_post (text, user_id, created_at) VALUES ('{text}', {user_instance.id}, '{created_at}')"
                    try:
                        with connection.cursor() as cursor:
                            cursor.execute(query)
                        messages.success(request, "Post added successfully!")
                    except Exception as e:
                        messages.error(request, "An error occurred while adding the post.")
            except User.DoesNotExist:
                messages.error(request, "User does not exist.")
        else:
            messages.error(request, "You need to be logged in to post.")

def add_comment(request, username, comment_text, post_id):
    if len(comment_text) == 0:
        messages.error(request, "Comment can't be empty")
        return
    created_at = timezone.now().strftime('%Y-%m-%d') 
    user_instance = User.objects.get(username=username)
    post_instance = Post.objects.get(id=post_id)

    comment = Comment.objects.create(comment_text=comment_text, user=user_instance, post=post_instance, created_at=created_at)
    comment.save()
    return True

