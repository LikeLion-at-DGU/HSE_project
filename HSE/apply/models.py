from django.db import models
from django.contrib.auth.models import User
from education.models import EduPost
# Create your models here.

class apply(models.Model):
    applicant= models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    phone_num= models.CharField(max_length=11)
    title=models.CharField(max_length=200)
    main_or_sub = models.CharField(max_length=10)
    winner=models.CharField(max_length=10, default='')
    
    # def __str__(self):
    #     return self.applicant


