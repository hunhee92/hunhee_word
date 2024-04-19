from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, update_session_auth_hash
from django.contrib.auth import logout as auth_logout
from . foms import CustomUserCreationForm, ProfileImageForm
from . models import CustomUser
from django.views.decorators.http import require_POST, require_http_methods
from products.models import Products
from django.db.models import Count
# Create your views here.


def index(request):
    product = Products.objects.annotate(
        like_count=Count('like')
    ).order_by('-like_count', '-created_at')

    context = {
        'product': product,
    }
    return render(request, "accounts/index.html", context)


def login(request):
    c_form = CustomUserCreationForm()
    form = AuthenticationForm()
    context = {"form": form,
               "c_form": c_form}
    return render(request, "accounts/login.html", context)


def u_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_url = request.GET.get('next') or 'products:products'
            return redirect(next_url)
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:login")
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, "accounts/login.html", context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("accounts:index")


def u_update(request, pk):

    u_profile = CustomUser.objects.get(pk=pk)
    if request.method == "POST":
        print("포스트 들어옴")
        form = ProfileImageForm(
            request.POST, request.FILES, instance=u_profile)
        if form.is_valid():
            u_profile = form.save()
            print("세이브 됨")
            return redirect("products:profile", u_profile.pk)
        else:
            print("유효성실패", form.errors)
    else:
        form = CustomUserCreationForm(instance=u_profile)

    context = {'form': form,
               'u_profile': u_profile,
               }
    return render(request, "products/profile.html", context)


def follow_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    print("들어왓다 ", "팔로우 대상:", user, pk)
    request.user.follow(user)
    next_page = request.POST.get('next') or 'products:product'
    print(next_page, "왜 자꾸 프로필로 가지냐")
    return redirect(next_page)


def unfollow_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    request.user.unfollow(user)
    next_page = request.POST.get('next') or 'products:product'
    return redirect(next_page)
