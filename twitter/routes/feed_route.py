from django.shortcuts import render
from twitter.decorators import login_required
from twitter.models import Post

@login_required
def home(request):
    posts = Post.objects.all().order_by("-created_at")  
    return render(request, "feed.html", {"posts": posts})
