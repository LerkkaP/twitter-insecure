from ..models import Post, User
from django.contrib import messages

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