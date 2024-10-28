from django.shortcuts import render, redirect, get_object_or_404
from twitter.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from ..views.post import add_post, add_comment
from ..models import Post

@login_required
@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        username = request.session.get('username')
        add_post(request, text, username)
        return redirect(reverse('home'))  
    return render(request, 'feed.html')

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all() 
    if request.method == 'GET':

        return render(request, 'post_detail.html', {
            'post': post,
            'comments': comments,
        })
    
    if request.method == 'POST':
        username = request.session.get('username')
        comment_text = request.POST.get('comment_text')
        
        add_comment(request, username, comment_text, post_id)

        return redirect('post_detail', post_id=post.id)

