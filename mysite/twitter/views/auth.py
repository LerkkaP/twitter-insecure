from ..models import User
from django.contrib import messages

def register_user(request, username, password1, password2):
    errors = []

    if len(username) < 4:
        errors.append("Username must be at least 4 characters long")

    if len(password1) < 4:
        errors.append("Password must be at least 4 characters long")

    if password1 != password2:
        errors.append("Passwords do not match")

    if User.objects.filter(username=username).exists():
        errors.append("Username is already taken")

    if errors:
        for error in errors:
            messages.add_message(request, messages.ERROR, error, extra_tags='signup')
        return False

    user = User.objects.create(username=username, password=password1)
    user.save()
    request.session['username'] = username
    return True

def login_user(request, username, password):
    credentials = User.objects.filter(username=username).values('username', 'password').first()

    if credentials is not None:
        if credentials['username'] == username and credentials['password'] == password:
            request.session['username'] = username
            return True
    
    messages.add_message(request, messages.ERROR, "Invalid username or password", extra_tags='login')
    return False
    


   
