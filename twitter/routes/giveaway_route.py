from django.shortcuts import render

def giveaway(request):
    return render(request, 'giveaway.html')