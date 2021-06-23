from django.contrib.auth.models import User
from django import forms
from .models import Profile
from allauth.account.forms import LoginForm

class SignupForm(forms.Form):
    model=User

    name = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'placeholder':'name'}))

    def signup(self, request, user):
        profile=Profile()
        profile.user = user
        profile.name = self.cleaned_data['이름']
        profile.save()
        user.save()
        return user

class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['login'].widget = forms.TextInput(attrs={'type':'text',
                                        'placeholder':'아이디', 'autofocus':'autofocus', 'class':'form-control'})