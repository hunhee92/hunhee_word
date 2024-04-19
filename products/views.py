from django.shortcuts import get_object_or_404, render, redirect
from accounts.foms import CustomUserCreationForm, ProfileImageForm
from .foms import ProductForm
from .models import Products
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.db.models import Count
from django.db.models import Q

# Create your views here.


def products(request):
    products = Products.objects.annotate(
        like_count=Count('like')
    ).order_by('-like_count', '-created_at')[:4]
    new_product = Products.objects.all().order_by('-created_at')[:4]
    context = {
        'products': products,
        'new_product': new_product,
    }
    return render(request, "products/products.html", context)


def post(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, "products/post.html", context)


def like_post(request):
    products = products = Products.objects.annotate(
        like_count=Count('like')
    ).order_by('-like_count', '-created_at')
    context = {'products': products}
    return render(request, "products/post.html", context)


def new_post(request):
    products = Products.objects.all().order_by('-created_at')
    context = {'products': products}
    return render(request, "products/post.html", context)


def c_post(request):
    forms = ProductForm()
    context = {'forms': forms}
    return render(request, 'products/c_post.html', context)


@login_required
def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect("products:post_detail", article.pk)

    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, "products/c_post.html", context)


def post_detail(request, pk):

    product = get_object_or_404(Products, pk=pk)
    account = product.user
    product.post_count += 1
    product.save()

    other_products = account.user.exclude(id=pk)
    context = {
        'product': product,
        'pk': pk,
        'other_products': other_products,
    }
    return render(request, 'products/post_detail.html', context)


@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        poduct = get_object_or_404(Products, pk=pk)
        poduct.delete()
    return redirect('products:products')


def update(request, pk):
    poroduct = Products.objects.get(pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=poroduct)
        if form.is_valid():
            poroduct = form.save()
            return redirect("products:post_detail", poroduct.pk)
    else:
        form = ProductForm(instance=poroduct)

    context = {'form': form,
               'product': poroduct,
               }
    return render(request, "products/update.html", context)


def add_like(request, pk):
    product = get_object_or_404(Products, pk=pk)
    user = request.user
    if product not in user.like.all():
        user.like.add(product)
    else:
        user.like.remove(product)
    return redirect('products:post_detail', pk=pk)


def profile(request, pk):
    c_form = ProfileImageForm()
    profile = get_object_or_404(CustomUser, pk=pk)
    liked = request.user.like.all()
    account = profile.user.all().order_by("-pk")
    user = CustomUser.objects.get(pk=pk)
    followers = user.get_followers
    following = user.get_following
    context = {"profile": profile,
               "liked": liked,
               "c_form": c_form,
               "account": account,
               "followers": followers,
               "following": following,
               }

    return render(request, "products/profile.html", context)


def search_results(request):
    query = request.GET.get('query', '')
    print("검색어", query)
    msg = "검색 결과가 없습니다"
    if query:
        products = Products.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    context = {
        'products': products,
        "msg": msg
    }
    return render(request, 'products/post.html', context)
