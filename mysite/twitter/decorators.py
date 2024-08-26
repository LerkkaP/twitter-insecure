from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse

def login_required(f):
    @wraps(f)
    def wrap(request, *args, **kwargs):
        username = request.session.get("username")
        if not username:
            return redirect(reverse('index'))
        return f(request, *args, **kwargs)
    return wrap