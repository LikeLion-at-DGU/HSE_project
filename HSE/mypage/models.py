from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 사용자
    name = models.CharField(max_length=64, default="") # 사용자 이름