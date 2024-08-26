from django.urls import path
from .routes.index_route import index
from .routes.feed_route import feed
from .routes.auth import register
from .routes.auth import logout


urlpatterns = [
    path('', index, name='index'),
    path('feed/', feed, name='feed'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    ]
