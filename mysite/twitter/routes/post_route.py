from django.shortcuts import render, redirect, get_object_or_404
from twitter.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from ..views.post import add_post
from ..models import Post

@login_required
@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        username = request.session.get('username')
        print(username)
        add_post(request, text, username)
        return redirect(reverse('home'))  
    return render(request, 'feed.html')

def post_detail(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, id=post_id)

        return render(request, 'post_detail.html', {
            'post': post
        })
