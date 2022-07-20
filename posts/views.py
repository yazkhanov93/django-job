from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from posts.forms import ExperienceForm, EducationForm, PostForm

from .models import *


def index(request):
    return render(request, "index.html")


def experienceForm(request):
    form = ExperienceForm()
    if request.method == "POST":
        form = ExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("my_profile")
        else:
            messages.warning(request, "Fill required fields !!!")
    return render(request, "experience_form.html", {"form":form})


def educationForm(request):
    form = EducationForm()
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my_profile")
        else:
            messages.warning(request, "Fill required fields !!!")
    return render(request, "education_form.html", {"form":form})


def addPost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("my_profile")
        else:
            messages.warning(request, "Fill required fields !!!")
    return render(request,"post_form.html", {"form":form})


def editPost(request, pk):
    form = Post.objects.get(id=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=form)
        if form.is_valid():
            form.save()
            return redirect("my_profile")
        else:
            messages.warning(request, "Fill required feilds !!!")
    return render(request, "post_form.html", {"form":PostForm(instance=form)})


def postDetail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "post_detail.html", {"post_detail":post})