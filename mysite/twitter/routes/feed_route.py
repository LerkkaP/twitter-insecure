from django.shortcuts import render
from twitter.decorators import login_required
from ..models import Post

@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')  
    print(posts)
    return render(request, 'feed.html', {'posts': posts})
