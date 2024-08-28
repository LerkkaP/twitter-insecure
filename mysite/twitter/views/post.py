from ..models import Post
from ..models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

def add_post(request, username, text):
    if request.method == 'POST':
        text = request.POST.get('text')
        username = request.session.get('username')  # Fetch username from session
        if username:
            try:
                user_instance = User.objects.get(username=username)
                if len(text) > 280:
                    messages.error(request, "Max length 280 characters!")
                else:
                    Post.objects.create(text=text, user=user_instance)
                    messages.success(request, "Post added successfully!")
            except User.DoesNotExist:
                messages.error(request, "User does not exist.")
        else:
            messages.error(request, "You need to be logged in to post.")
        
    return redirect(reverse('home'))  # Redirect to the feed page to show the updated posts





