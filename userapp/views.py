from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from customuser.settings import AUTH_USER_MODEL
from .forms import LoginForm, SignupForm
from .models import MyUser
# Create your views here.
@login_required
def index(request):
    user = request.user
    return render(request, 'index.html', {"user": user, "auth_user_model":AUTH_USER_MODEL, "logout_url":reverse('logout')})

def loginview(request):
    html = "login.html"

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    
    form = LoginForm()
    return render(request, html, {"form": form, "signup_url":reverse('signup')})

def signupview(request):
    html = "signup.html"

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(
                data['username'],
                data['display_name'],
                data['password'],
                None,
                data['age']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    
    form = SignupForm()
    return render(request, html, {"form":form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))