from ..models import Post, User, Comment
from django.contrib import messages
from django.utils import timezone
from django.db import connection

def add_post(request, text):
    if request.method == "POST":
        text = request.POST.get("text")
        user_id = request.session.get("user_id")
        if user_id:
            user_instance = User.objects.get(id=user_id)
            if len(text) == 0:
                print("Post cannot be empty")
                return None
            if len(text) > 280:
                print("Max post length is 280 characters")
                return None
            else:
                created_at = timezone.now().strftime("%Y-%m-%d")
                query = f"INSERT INTO twitter_post (text, user_id, created_at) VALUES ('{text}', {user_instance.id}, '{created_at}')"
                cursor = connection.cursor()
                cursor.execute(query)
                # Post.objects.create(text=text, user=user_instance, created_at=created_at)
                print("Post added successfully!")

def add_comment(request, comment_text, post_id):
    if len(comment_text) == 0:
        messages.error(request, "Comment can't be empty")
        print("Comment cannot be empty")
        return False
    user_id = request.session.get("user_id")
    user = User.objects.filter(id=user_id).values("username").first()
    username = user["username"]
    created_at = timezone.now().strftime("%Y-%m-%d") 
    user_instance = User.objects.get(username=username)
    post_instance = Post.objects.get(id=post_id)

    comment = Comment.objects.create(comment_text=comment_text, user=user_instance, post=post_instance, created_at=created_at)
    comment.save()
    return True

def delete_post(request, post_id):
    post_to_delete = Post.objects.get(id=post_id)
    # post_user_id = post_to_delete.user.id
    # user_id = request.session.get("user_id")
    # if user_id == post_user_id:
        # post_to_dete.delete()
    post_to_delete.delete()
  

