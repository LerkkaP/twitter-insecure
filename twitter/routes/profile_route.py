from django.shortcuts import render
from twitter.decorators import login_required
from ..models import Post

@login_required
def show_profile(request, user_id):
    if request.method == "GET":
        posts = Post.objects.filter(user_id=user_id).order_by("-created_at")
        return render(request, "profile.html", {"posts": posts})

