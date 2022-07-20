from django.urls import path
from . import views

urlpatterns  = [
    path("sign_up/", views.signUp, name="sign_up"),
    path("sign_in/", views.signIn, name="sign_in"),
    path("sign_out/", views.signOut, name="sign_out"),
    path("create_profile/", views.createProfile, name="create_profile"),
    path("my_profile/", views.myProfile, name="my_profile"),
    path("profile_setting/", views.profileSetting, name="profile_setting"),
]