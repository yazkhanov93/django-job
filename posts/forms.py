from django import forms
from django.contrib.auth.models import User

from .models import *


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ["user", "title", "company_name", "years"]

        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"Job position"}),
            "company_name": forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"Company name"}),
            "years" : forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"years"})
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ["user", "title", "university","department","degree","years"]

        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"speciality"}),
            "university": forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"University name"}),
            "department": forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"Department name"}),
            "degree": forms.Select(attrs={"class":"form-control mb-2", "placeholder":"Degree"}),
            "years" : forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"years"})
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["user","title","body","image"]

        widgets = {
            "title": forms.TextInput(attrs={"class":"form-control mb-2","placeholder":"title"}),
            "body":forms.Textarea(attrs={"class":"form-control mb-2", "placeholder":"Context"}),
            "image":forms.FileInput(attrs={"class":"form-control mb-2",})
        }


# class VacancyForm(forms.ModelForm):
#     class Meta:
#         model = 