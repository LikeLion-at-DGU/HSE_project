from django.db import models
from allauth.account.forms import LoginForm

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.writer