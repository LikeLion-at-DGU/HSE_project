from django.contrib.auth.models import User
from django import forms
from .models import Profile


class SignupForm(forms.Form):
    model = User

    name = forms.CharField(
        max_length=64, widget=forms.TextInput(attrs={"placeholder": "name"})
    )

    def signup(self, request, user):
        profile = Profile()
        profile.user = user
        profile.name = self.cleaned_data["name"]
        profile.save()
        user.save()
        return user