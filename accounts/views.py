from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, update_session_auth_hash
from django.contrib.auth import logout as auth_logout
from . foms import CustomUserCreationForm
from django.views.decorators.http import require_POST, require_http_methods
# Create your views here.


def index(request):
    return render(request, "accounts/index.html")


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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accouts:login")
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, "accounts/login.html", context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("accounts:index")
