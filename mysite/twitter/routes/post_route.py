from django.shortcuts import render, redirect
from twitter.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from ..views.post import add_post

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

