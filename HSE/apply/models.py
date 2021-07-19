from django.db import models
from django.contrib.auth.models import User
from education.models import EduPost
# Create your models here.

class apply(models.Model):
    applicant= models.ForeignKey(User, on_delete=models.CASCADE) # 봉사지원자
    name=models.CharField(max_length=20) # 봉사자 성함
    phone_num= models.CharField(max_length=11) # 봉사자 핸드폰번호
    title=models.CharField(max_length=200) # 봉사명
    main_or_sub = models.CharField(max_length=10) # 주봉사로 신청할지 보조봉사자로 신청할지
    winner=models.CharField(max_length=10, default='') # 당첨된 봉사자
    total_work= models.IntegerField(default=0) # 봉사한 시간 
    total_count=models.IntegerField(default=0) # 봉사한 횟수
   


