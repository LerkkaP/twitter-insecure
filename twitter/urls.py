from django.urls import path

from twitter.routes.index_route import index
from twitter.routes.feed_route import home
from twitter.routes.auth import logout_user
from twitter.routes.auth import login
from twitter.routes.post_route import create_post, post_detail, remove_post
from twitter.routes.profile_route import show_profile
from twitter.routes.giveaway_route import giveaway

urlpatterns = [
    path("", index, name="index"),
    path("home/", home, name="home"),
    path("login/", login, name="login"),
    path("logout/", logout_user, name="logout"),
    path("create_post/", create_post, name="create_post"),
    path("post/<int:post_id>/", post_detail, name="post_detail"),  
    path("profile/<int:user_id>/", show_profile, name="profile"),
    path("post/<int:post_id>/remove/", remove_post, name="remove_post"),
    path("giveaway", giveaway, name="giveaway")
    ]
