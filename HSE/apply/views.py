from django.shortcuts import render, redirect, get_object_or_404
from .models import apply
from education.models import EduPost
import random
import datetime

    
def apply_main_sub(request, post_id): 
    post=get_object_or_404(EduPost,pk=post_id)
    return render(request, "apply/apply.html",{'post':post})
# 어떤 봉사에 지원을 할지 정해주기 위해서 post라는 변수에 지원하려는 봉사의 정보를 담아 지원하는 apply.html로 넘겨줌

def apply_new(request): 
    a=request.user
    b=request.POST['title']
    t=True
    for i in apply.objects.filter(title=b): # b에 봉사명을 담아 apply오브젝트중 해당 봉사명인 경우들을 불러 for문으로 확인
        if i.applicant == a: # 해당 봉사 지원자중에 현재 로그인하여 사용중인 사람의 정보가 있는경우 t라는 변수에 False값으로 초기화
            t=False
            break
        else:
            continue
    if t: # t=True라는 뜻은 해당 봉사에 지원한 이력이 없다는 뜻, 없다면 양식에 작성된 내용을 저장해줌
        new_apply = apply()
        new_apply.name = request.POST["name"]
        new_apply.phone_num = request.POST["phone_num"][-4:]
        new_apply.title=request.POST['title']
        new_apply.main_or_sub=request.POST['main_or_sub']
        new_apply.applicant = request.user
        new_apply.save()
        return redirect('education:edulist')
    else: # 이미 봉사에 지원한 경우 alert.html로 넘겨 경고 팝업으로 이미 신청했다는 것을 보여줌
        return render(request,'apply/alert.html')
# 해당 봉사에 이미 지원한지 확인후 지원하지않으면 지원완료, 이미 했다면 경고창을 띄워줌    
    
def apply_result(request,post_id):
    post=get_object_or_404(EduPost,pk=post_id)
    apply_o=apply.objects.all()
    if post.count==0: #사람들이 볼때마다 랜덤이 돌아가서 당첨자가 바뀌면 안되기 때문에 한번도 안확인한지 count가 0인지 확인함
        post.count+=1 #0을 기본값을고 갖고 있는 카운트에 1을 더해줌으로써 가장 처음 확인할때만 랜덤으로 당첨자를 선정하고 픽스 시키기 위한 부분
        post.save()
        
       
        m=[]
        s=[]
       
        m_o=apply_o.filter(title=post.title, main_or_sub='주강사')  # 현재 결과를 알고자하는 봉사에 지원한 사람중 주강사를 신청한 사람
        s_o=apply_o.filter(title=post.title, main_or_sub='보조강사') # 현재 결과를 알고자하는 봉사에 지원한 사람중 보조강사를 신청한 사람

        for i in m_o:  
            m.append(i)
        for i in s_o:
            s.append(i)
        # 랜덤하기위해 리스트에 담아줌
        if post.main_teacher < len(m):  # 지원받는 주강사 수보다 지원자 수가 많은 경우
            m=random.sample(m,post.main_teacher) #랜덤으로 주강사 수만큼 뽑고, 적은경우는 지원한 사람 모두 다 뽑음

        for i in m:
            i.winner='winner' # 당첨이 되었다는 것을 표시하기 위해
            i.total_work+=post.work_hour # 해당 봉사의 봉사시간을 당첨된 지원자에게 부여해줌
            i.total_count+=1 # 봉사를 할 예정이기에 한번 카운트 해줌
            i.save()
        
        if post.sub_teacher < len(s): # 지원받는 보조강사 수보다 지원자 수가 많은 경우
            s=random.sample(s,post.sub_teacher)  #랜덤으로 주강사 수만큼 뽑고, 적은경우는 지원한 사람 모두 다 뽑음
        
        for i in s:
            i.winner='winner' # 당첨이 되었다는 것을 표시하기 위해
            i.total_work+=post.work_hour # 해당 봉사의 봉사시간을 당첨된 지원자에게 부여해줌
            i.total_count+=1 # 봉사를 할 예정이기에 한번 카운트 해줌
            i.save()
            
    # 위에서는 맨처음 랜덤하여 선정하는 코드이고 아래에는 맨처음 확인하는 경우가 아니거나 맨처음 랜덤한 후 저장된 정보를 보여주는 부분

    # main_l=[]
    # sub_l=[]
    # for i in apply_o:
    #     if i.title  == post.title:
    #         if i.main_or_sub == "주강사":
    #             if i.winner=='winner':
    #                 # print(i.name,i.winner,'m')
                    
    #                 main_l.append(i)
    #         else:
    #             if i.winner=='winner':
    #                 # print(i.name,i.winner,'s')
                    
    #                 sub_l.append(i)


    main_l=apply_o.filter(title=post.title, winner='winner', main_or_sub="주강사")
    sub_l=apply_o.filter(title=post.title, winner='winner', main_or_sub="보조강사")

    # 당첨자들을 확인할수있는 조건들을 통해 당첨자 들을 따로 변수에 담아 result.html로 넘겨줌, 위에 for문으로도 가능하지만 orm 사용으로 고쳐둠

    return render(request, "apply/result.html",{"main": main_l, "sub":sub_l})