from django.shortcuts import render
from main.models import Post
from apply.models import apply
from django.contrib.auth.models import User

from .models import Profile
from apply.models import apply
from education.models import EduPost
from django.db.models import Sum, Count
# Create your views here.

def mypage(request):
    user = request.user
    myinfo=apply.objects.filter(applicant=user)
    #posts=Post.objects.filter(writer=user)
    #apply_title = request.myinfo.title
    #apply_title = request.title2
    result1 = apply.objects.filter(winner=user)
    #result2 = EduPost.objects.filter(title=apply_title)

    #result2.total_time = EduPost.objects.filter('work_hour').aggregate(Sum)
    #total_count = Profile.objects.values('pk').annotate(Count('pk'))
    
    #main_or_sub = result1.main_or_sub
    #if user == apply.winner:
    #result1.main_or_sub = apply.objects.filter('main_or_sub')
    #result1.title = apply.objects.filter('title')
    #result2.date = EduPost.objects.filter('work_date')
    #result2.hour = EduPost.objects.filter('work_hour')
    return render(request, 'mypage/mypage.html', {'myinfo':myinfo, 'result1':result1})
