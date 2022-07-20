from django.urls import path
from .import views

urlpatterns  = [
    path("", views.index, name="index"),
    path("add_experience/", views.experienceForm, name="add_experience"),
    path("add_education/", views.educationForm, name="add_education"),
    path("add_post/", views.addPost, name="add_post"),
    path("edit_post/<int:pk>/", views.editPost, name="edit_post"),
    path("post_detail/<int:pk>/", views.postDetail, name="post_detail")
]