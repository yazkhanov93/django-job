from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    birthday = forms.DateField(required=True, 
        widget=forms.DateInput(attrs={
            'placeholder':'Birth Date', 
            'class': 'form-control mb-2',
            'type': 'date',                                                                 
        }))
    # user = forms.CharField(required=True, widget=forms.TextInput(attrs={"type":"text", "name":"user", "value":"{{request.user}}"}))
    
    class Meta:
        model = Profile
        fields = ['user', 'firstname', 'lastname', 'image', 'phone', 'email', 'region', 'district','birthday','profession']

        widgets = {
            "firstname" : forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"Firtname"}),
            "lastname":forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"Lastname"}),
            "phone":forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"Mobile number"}),
            "email":forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"email"}),
            "profession":forms.TextInput(attrs={"class":"form-control mb-2", "placeholder":"profession"}),
            "image":forms.FileInput(attrs={"class":"form-control mb-2"}),
            "region": forms.Select(attrs={"class":"form-control mb-2", "placeholder":"region"}),
            "district": forms.Select(attrs={"class":"form-control mb-2", "placeholder":"district"}),
        }