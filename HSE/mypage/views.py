from django.shortcuts import render
from apply.models import apply
from django.contrib.auth.models import User
from .models import Profile
from education.models import EduPost
# Create your views here.

def mypage(request):
    
    user=request.user # 사용자 정보
    a=0
    b=0
    post=EduPost.objects.all() # 등록된 봉사 정보 가져와 post에 저장
    myinfo=apply.objects.filter(applicant=user) # 등록된 봉사의 신청자와 사용자가 동일할 경우, 해당 봉사 정보를 myinfo에 저장
    
    for i in myinfo:
        a+=int(i.total_work)
    # myinfo에 저장된 정보 중 봉사 시간 정보를 가져와 a에 누적 저장 -> 사용자의 총 봉사시간 계산
    
    for i in myinfo:
        b+=int(i.total_count)
    # myinfo에 저장된 정보 중 봉사한 횟수를 b에 누적하여 저장 -> 사용자의 총 봉사 참여 횟수 계산

    return render(request, 'mypage/mypage.html', {'myinfo':myinfo,'a':a,'b':b, 'post':post})
    # 사용자의 봉사 참여 내역을 mypage.html에 넘겨줌