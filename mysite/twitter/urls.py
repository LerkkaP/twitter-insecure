from django.urls import path

from .routes.index_route import index
from .routes.feed_route import home
from .routes.auth import register
from .routes.auth import logout
from .routes.auth import login
from .routes.post_route import create_post, post_detail, remove_post
from .routes.profile_route import show_profile


urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('create_post/', create_post, name='create_post'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),  
    path('profile/<int:user_id>/', show_profile, name='profile'),
    path('post/<int:post_id>/remove/', remove_post, name='remove_post'),  # Add this line

    ]
