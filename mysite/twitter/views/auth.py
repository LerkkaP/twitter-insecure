from ..models import User
from django.contrib import messages

def login_user(request, username, password):
    user = User.objects.filter(username=username).values("id","username", "password").first()

    if user is not None:
        if user["username"] == username and user["password"] == password:
            request.session["user_id"] = user["id"]
            request.session["username"] = user["username"]
            return True
    
    messages.add_message(request, messages.ERROR, "Invalid username or password", extra_tags="login")
    return False
    


   
