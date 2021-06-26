from django.shortcuts import render
from main.models import Post
from apply.models import apply
from django.contrib.auth.models import User
# Create your views here.

def mypage(request):
    
    user=request.user
    
    myinfo=apply.objects.get(applicant=user)

    return render(request, 'mypage/mypage.html', {'myinfo':myinfo})
