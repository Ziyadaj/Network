
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/<str:user_name>", views.profile, name="profile"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    #API Routes
    path("post", views.form, name="post"),
    path("post/<int:post_id>", views.edit, name="edit"),
    # path("feed/<int:post_id>/like", views.like, name="like"),
]
