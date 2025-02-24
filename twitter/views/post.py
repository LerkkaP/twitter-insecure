from twitter.models import Post, User, Comment
from django.contrib import messages
from django.utils import timezone
from django.db import connection
from django.shortcuts import get_object_or_404

def add_post(request, text):
    if request.method == "POST":
        text = request.POST.get("text")
        user_instance = request.user
        if len(text) == 0:
            print("Post cannot be empty")
            return None
        if len(text) > 280:
            print("Max post length is 280 characters")
            return None
        else:
            created_at = timezone.now()
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
    created_at = timezone.now().strftime("%Y-%m-%d") 
    user_instance = request.user
    post_instance = Post.objects.get(id=post_id)

    comment = Comment.objects.create(comment_text=comment_text, user=user_instance, post=post_instance, created_at=created_at)
    comment.save()
    return True

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    #post_owner = post.user.id
    #user_id = request.user.id
    #if user_id == post_owner:
        #post.delete()

def get_posts():
    posts = Post.objects.all().order_by("-created_at")  
    return posts

def get_post_details(post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by("-created_at")
    return post, comments

def get_profile_posts(user_id):
    posts = Post.objects.filter(user_id=user_id).order_by("-created_at")
    return posts

