from django.shortcuts import render
from twitter.decorators import login_required

@login_required
def show_profile(request, user_id):
    print(user_id)
    if request.method == 'GET':
        return render(request, 'profile.html')
