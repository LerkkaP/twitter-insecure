from django.shortcuts import render, redirect
from twitter.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from twitter.views.post import add_post, add_comment, delete_post, get_post_details
from django.views.decorators.csrf import csrf_exempt

@login_required
@csrf_exempt
def create_post(request):
    if request.method == "POST":
        text = request.POST.get("text")
        add_post(request, text)
        return redirect(reverse("home"))  
    return render(request, "feed.html")

@login_required
def post_detail(request, post_id):
    post, comments = get_post_details(post_id)
    if request.method == "GET":

        return render(request, "post_detail.html", {
            "post": post,
            "comments": comments,
        })
    
    if request.method == "POST":
        comment_text = request.POST.get("comment_text")
        
        add_comment(request, comment_text, post_id)

        return redirect("post_detail", post_id=post.id)

@login_required
@csrf_exempt
def remove_post(request, post_id):
    if request.method == "POST":
        delete_post(request, post_id)
        user_id = request.user.id
        return redirect("profile", user_id=user_id)
    return render(request, "feed.html")