from django.urls import path
from .import views

app_name="mypage"
urlpatterns=[
    path('mypage/', views.mypage, name="mypage")
]