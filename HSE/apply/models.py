from django.db import models
from django.contrib.auth.models import User
from education.models import EduPost
# Create your models here.

class apply(models.Model):
    applicant= models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    phone_num= models.IntegerField(max_length=20)
    title=models.CharField(max_length=200)
    main_or_sub = models.CharField(max_length=10)
    HS=models.ForeignKey(EduPost,on_delete=models.CASCADE)
    # count = models.IntegerField(default=0) 인스턴스변수로 개개인 카운트할지 생각해보기

    def __str__(self):
        return self.applicant

    