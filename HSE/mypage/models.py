from django.db import models
from django.contrib.auth.models import User
from apply.models import apply

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, default="")

    #number=models.IntegerField(default=0)
    #title=models.CharField(max_length=200)
    #main_or_sub = models.CharField(max_length=10)
    #date = models.DateField()
    #hour = models.IntegerField(default=0)