from django.shortcuts import render
from twitter.decorators import login_required
from twitter.views.post import get_profile_posts

@login_required
def show_profile(request, user_id):
    if request.method == "GET":
        posts = get_profile_posts(user_id)
        return render(request, "profile.html", {"posts": posts})

