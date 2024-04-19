from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("products/", views.products, name="products"),
    path("post/", views.post, name="post"),
    path("new_post/", views.new_post, name="new_post"),
    path("like_post/", views.like_post, name="like_post"),
    path("c_post/", views.c_post, name="c_post"),
    path("create/", views.create, name="create"),
    path("post_detail/<int:pk>/", views.post_detail, name="post_detail"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("update/<int:pk>/", views.update, name="update"),
    path("add_like/<int:pk>/", views.add_like, name="add_like"),
    path("profile/<int:pk>/", views.profile, name='profile'),
    path("search_results/", views.search_results, name='search_results'),
]
