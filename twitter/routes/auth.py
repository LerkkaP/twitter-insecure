from django.shortcuts import render, redirect
from django.urls import reverse
from twitter.views.auth import login_user

def logout(request):
    del request.session["user_id"]
    return redirect(reverse("index"))

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        success = login_user(request, username, password)

        if success:
            return redirect("/home")
        return render(request, "index.html", {
            "login_modal_open": True,
            "form_data": {
                "username": username,
                "password": password
            }
        })


