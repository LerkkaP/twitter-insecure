from django.shortcuts import render
from twitter.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
#from ..views.post import add_post

@login_required
@csrf_exempt
def create_post(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        user = request.session['username']
        print(text, user)
    return render(request, 'feed.html')

