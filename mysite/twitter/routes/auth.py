from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from ..views.auth import register_user
from ..views.auth import login_user

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        success = register_user(request, username, password1, password2)

        if success:
            return redirect('/home')
        return render(request, 'index.html', {
            'signup_modal_open': True,
            'form_data': {
                'username': username,
                'password1': password1,
                'password2': password2
            }
        })

    return render(request, 'index.html')

def logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect(reverse('index'))

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        success = login_user(request, username, password)

        if success:
            return redirect('/home')
        return render(request, 'index.html', {
            'login_modal_open': True,
            'form_data': {
                'username': username,
                'password': password
            }
        })


