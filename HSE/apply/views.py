from django.shortcuts import render, redirect, get_object_or_404
from .models import apply
from education.models import EduPost
import random
import datetime

def apply_detail(request, id):
    post = get_object_or_404(EduPost, pk=id)
    date=post.due_date
    rn = datetime.datetime.now()
    rn=rn.strftime('%y-%m-%d %H:%M:%S')
    rn=datetime.datetime.strptime(rn,'%y-%m-%d %H:%M:%S')
   
    if date>=rn:
        t=True
    else:
        t=False

    return render(request, "apply/apply.html", {"post": post, "rn":t})


def apply_main(request):
    return render(request, "apply/main.html")

def apply_sub(request):
    return render(request, "apply/sub.html")

def apply_new(request):
    new_apply = apply()
    new_apply.name = request.POST["name"]
    new_apply.phone_num = request.POST["phone_num"]
    new_apply.title=request.POST['title']
    new_apply.main_or_sub=request.POST['main_or_sub']
    new_apply.applicant = request.user
    new_apply.save()
    return render(request,'apply/main.html')


def apply_result(request,post_id):
    post=get_object_or_404(EduPost,pk=post_id)
    apply_o=apply.objects.all()
    t=[] #특정(현재 post_id 봉사관련) db 만 골라내기
    main_l=[]
    sub_l=[]

    for i in apply_o:
        if i.title  == post.title:
            t.append(i)
    for i in t:
        if i.main_or_sub == '주봉사':
            main_l.append(i)
        else:
            sub_l.append(i)

    if post.main_teacher < len(main_l): 
        main_l=random(main_l,post.main_teacher) #아니면 다뽑음
    
    if post.sub_teacher < len(sub_l): 
        sub_l=random(sub_l,post.sub_teacher)  #아니면다뽑음

    return render(request, "apply/result.html",{"main": main_l, "sub":sub_l})