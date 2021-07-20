from django.contrib.auth.models import User
from django import forms
from .models import Profile

# 회원가입
class SignupForm(forms.Form):
    model = User

    name = forms.CharField(
        max_length=64, widget=forms.TextInput(attrs={"placeholder": "name"})
    )

    def signup(self, request, user):
        profile = Profile() # 프로필 모델 가져옴
        profile.user = user # 사용자 정보(아이디, 비밀번호)
        profile.name = self.cleaned_data["name"] # 사용자 이름
        profile.save()
        user.save()
        return user