from django.shortcuts import render
from twitter.decorators import login_required

@login_required
def home(request):
    return render(request, 'base.html')

