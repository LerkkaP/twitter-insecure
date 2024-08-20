from django.urls import path
from .routes.index_route import index
from .routes.login_route import login

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login')
]

"""urlpatterns = [
    path('', views.index, name='index'),
    path('/signin', views.sign_in, name='sign_in')
]"""

"""path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path('watches', views.watches, name="watches"),
    path('details/<int:id>', views.details, name='details'),
    path('watch/<int:id>/handle_description/', views.handle_description, name='handle_description'),
    path('add_watch/', views.add_watch, name='add_watch'),
    path('details/<int:id>/delete_watch/', views.delete_watch, name='delete_watch')"""