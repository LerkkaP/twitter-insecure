from django.shortcuts import render
from twitter.decorators import login_required

@login_required
def feed(request):
    return render(request, 'base.html')

