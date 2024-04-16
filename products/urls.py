from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("products/", views.products, name="products"),
    path("c_post/", views.c_post, name="c_post"),
]
