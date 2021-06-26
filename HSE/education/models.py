from django.db import models
from django.db.models.aggregates import Max
from django.contrib.auth.models import User

# Create your models here.
class EduPost(models.Model):
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    due_date = models.DateTimeField()
    main_teacher = models.IntegerField()
    sub_teacher = models.IntegerField()
    work_hour = models.IntegerField()
    body = models.TextField()
    video = models.CharField(null=True, max_length=200)
    extrafile = models.FileField(upload_to="extrafiles/", null=True)
    count = models.IntegerField(default=0)
