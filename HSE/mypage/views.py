from django.shortcuts import render
from main.models import Post
from apply.models import apply
from django.contrib.auth.models import User
# Create your views here.

def mypage(request):
    
    user=request.user
    a=0
    b=0
    myinfo=apply.objects.filter(applicant=user)
    for i in myinfo:
        a+=int(i.total_work)
    
    for i in myinfo:
        b+=int(i.total_count)
    
    return render(request, 'mypage/mypage.html', {'myinfo':myinfo,'a':a,'b':b})
