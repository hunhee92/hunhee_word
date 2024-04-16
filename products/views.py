from django.shortcuts import render
from .foms import ProductForm
# Create your views here.


def products(request):
    return render(request, "products/products.html")


def c_post(request):
    foms = ProductForm()
    context = {'foms': foms}
    return render(request, 'products/c_post.html', context)
