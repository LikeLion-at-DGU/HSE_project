from django.shortcuts import render
from main.models import Post
from django.contrib.auth.models import User

from .models import Profile
from apply.models import apply
from django.db.models import Sum, Count
# Create your views here.

def mypage(request):
    user = request.user
    posts=Post.objects.filter(writer=user)

    #total_time = Profile.objects.values('hour').aggregate(Sum)
    #total_count = Profile.objects.values('pk').annotate(Count('pk'))
    
    #if user == apply.applicant:
        #main_or_sub = request.apply['main_or_sub']
        #title = request.apply['title']
        #date = request.apply['date']
        #hour = request.apply['hour']
    return render(request, 'mypage/mypage.html', {'posts':posts})
