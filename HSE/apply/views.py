from django.shortcuts import render, redirect, get_object_or_404
from .models import apply
from education.models import EduPost
import random
import datetime

count={}


def get_c(c):
    count[c]=0
class c:
    def __init__(self):
        self.main_l=[]
        self.sub_l=[]

    def get_m(self,z):
        self.main_l.append(z)
        
    def get_s(self,z):
        self.sub_l.append(z)
       
    def fin_m(self,z):
        self.main_l=z
        
        
    def fin_s(self,z):
        self.sub_l=z
        
    def put_m(self):
        
        return self.main_l
    def put_s(self):
        
        return self.sub_l

m=c()



def apply_main_sub(request, post_id):
    post=get_object_or_404(EduPost,pk=post_id)
    return render(request, "apply/apply.html",{'post':post})


def apply_new(request):
    new_apply = apply()
    new_apply.name = request.POST["name"]
    new_apply.phone_num = request.POST["phone_num"]
    new_apply.title=request.POST['title']
    new_apply.main_or_sub=request.POST['main_or_sub']
    new_apply.applicant = request.user
    new_apply.save()
    return redirect('education:edulist')


def apply_result(request,post_id):
    
    
    if count[post_id]==0:
        post=get_object_or_404(EduPost,pk=post_id)
        apply_o=apply.objects.all()
        
        t=[] #특정(현재 post_id 봉사관련) db 만 골라내기
       
        
        for i in apply_o:
            if i.title  == post.title:
                t.append(i)
        
        for i in t:
            if i.main_or_sub == '주강사':
                m.get_m(i)
            else:
                m.get_s(i)
        # for i in m.put_m():
        #     print("안에서 검사",i.name)   
        # for i in m.put_s():
        #     print("안에서 검사z",i.name) 

        if post.main_teacher < len(m.put_m()): 
            main_l=random.sample(m.put_m(),post.main_teacher) #아니면 다뽑음
           
            m.fin_m(main_l)
        if post.sub_teacher < len(m.put_s()): 
            sub_l=random.sample(m.put_s(),post.sub_teacher)  #아니면다뽑음
            
            m.fin_s(sub_l)
        count[post_id]+=1
        
    else:
       
        main_l=m.put_m()
        sub_l=m.put_s()
    # for i in main_l:
    #     print("main",i.name)
    # for i in sub_l:
    #     print("sub",i.name)
    return render(request, "apply/result.html",{"main": main_l, "sub":sub_l})