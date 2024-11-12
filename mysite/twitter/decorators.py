from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse

def login_required(f):
    @wraps(f)
    def wrap(request, *args, **kwargs):
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect(reverse('index'))
        return f(request, *args, **kwargs)
    return wrap