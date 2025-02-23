from django.contrib import messages
from django.contrib.auth import authenticate, login


def login_user(request, username, password):
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return True
    
    messages.add_message(request, messages.ERROR, "Invalid username or password", extra_tags="login")
    return False
    