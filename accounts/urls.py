from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path("", views.index, name='index'),
    path("login/", views.login, name="login"),
    path("u_login/", views.u_login, name="u_login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("u_update/<int:pk>", views.u_update, name="u_update"),
    path("follow_user/<int:pk>", views.follow_user, name="follow_user"),
    path("unfollow_user/<int:pk>", views.unfollow_user, name="unfollow_user"),
]
