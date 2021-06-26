from django.shortcuts import render, redirect, get_object_or_404
from .models import apply
from education.models import EduPost
import random
import datetime

    
def apply_main_sub(request, post_id):
    post=get_object_or_404(EduPost,pk=post_id)
    apply_o=apply.objects.all()
    return render(request, "apply/apply.html",{'post':post,'apply':apply_o})


def apply_new(request):
    a=request.user
    b=request.POST['title']
    t=True
    for i in apply.objects.filter(title=b):
        if i.applicant == a:
            t=False
            break
        else:
            continue
    if t:
        new_apply = apply()
        new_apply.name = request.POST["name"]
        new_apply.phone_num = request.POST["phone_num"][-4:]
        new_apply.title=request.POST['title']
        new_apply.main_or_sub=request.POST['main_or_sub']
        new_apply.applicant = request.user
        
        new_apply.save()
        
        
        return redirect('education:edulist')
    else:
        # print("hi")
        return render(request,'apply/alert.html')
    
    
def apply_result(request,post_id):
    post=get_object_or_404(EduPost,pk=post_id)
    apply_o=apply.objects.all()
    if post.count==0:
        post.count+=1
        post.save()
        
        
        t=[] #특정(현재 post_id 봉사관련) db 만 골라내기
        m=[]
        s=[]
        for i in apply_o:
            if i.title  == post.title:
                t.append(i)
                
        for i in t:
            if i.main_or_sub == '주강사':
                m.append(i)
                # print(i.name,'hi')
            else:
                s.append(i)
                # print(i.name,'hii')

        if post.main_teacher < len(m): 
            m=random.sample(m,post.main_teacher) #아니면 다뽑음 
        for i in m:
            i.winner='winner'
            i.total_work+=post.work_hour
            i.total_count+=1
            i.save()
            
        # print('len길이m',len(m))
        if post.sub_teacher < len(s): 
            s=random.sample(s,post.sub_teacher)  #아니면다뽑음
        # print('len길이s',len(s))
        for i in s:
            i.winner='winner'
            i.total_work+=post.work_hour
            i.total_count+=1
            i.save()
            
        
    main_l=[]
    sub_l=[]
    for i in apply_o:
        if i.title  == post.title:
            if i.main_or_sub == "주강사":
                if i.winner=='winner':
                    # print(i.name,i.winner,'m')
                    
                    main_l.append(i)
            else:
                if i.winner=='winner':
                    # print(i.name,i.winner,'s')
                    
                    sub_l.append(i)
   

    return render(request, "apply/result.html",{"main": main_l, "sub":sub_l})