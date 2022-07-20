from email import message
from pyexpat.errors import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import *
from .forms import *
from posts.models import *

def signUp(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("ok")
            return redirect("sign_in")
    return render(request, "sign_up.html", {"form":form})


def signIn(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, "profile"):
                return redirect("index")
            else:
                return redirect("create_profile")
        else:
            messages.warning(request, "Invalid username or password !!!")
    return render(request, "sign_in.html", {})


def signOut(request):
    logout(request)
    return redirect("/")



def createProfile(request):
    user = get_object_or_404(User, id=request.user.id)
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
        else:
            messages.warning(request, "Fill required fields !!!")
    return render(request, "profile_form.html", {"form":form})


def myProfile(request):
    user = get_object_or_404(User, id=request.user.id)
    profile = Profile.objects.get(user=user)
    experience = Experience.objects.filter(user=user)
    education = Education.objects.filter(user=user)
    post = Post.objects.filter(user=user)
    context = {
        "profile":profile,
        "experience":experience,
        "education":education,
        "post": post,
    }
    return render(request, "profile.html", context)


def profileSetting(request):
    profile = Profile.objects.get(user=request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('my_profile')
    return render(request, 'profile_form.html', {'form': ProfileForm(instance=profile)})