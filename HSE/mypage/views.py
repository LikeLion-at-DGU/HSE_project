from django.shortcuts import render
from apply.models import apply
from django.contrib.auth.models import User
from .models import Profile
from education.models import EduPost
# Create your views here.

def mypage(request):
    
    user=request.user
    a=0
    b=0
    post=EduPost.objects.all()
    myinfo=apply.objects.filter(applicant=user)
    for i in myinfo:
        a+=int(i.total_work)
    
    for i in myinfo:
        b+=int(i.total_count)
    return render(request, 'mypage/mypage.html', {'myinfo':myinfo,'a':a,'b':b, 'post':post})
