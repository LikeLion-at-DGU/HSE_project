from django.urls import path
from .import views

app_name="mypage"

urlpatterns=[
    path('mypage/', views.mypage, name="mypage")    # 사용자 프로필 보여주는 mypage
]