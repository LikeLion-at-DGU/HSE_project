from django.shortcuts import render
from main.models import Post
from django.contrib.auth.models import User
# Create your views here.

def mypage(request):
    user = request.user
    posts=Post.objects.filter(writer=user)
    return render(request, 'mypage/mypage.html', {'posts':posts})
