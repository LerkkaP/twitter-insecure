from django.shortcuts import render
from twitter.decorators import login_required
from twitter.views.post import get_posts

@login_required
def home(request):
    posts = get_posts() 
    return render(request, "feed.html", {"posts": posts})
