from django.urls import path
from . import views

app_name = "apply"
urlpatterns = [
   

    path('apply_main_sub/<int:post_id>',views.apply_main_sub, name="apply_main_sub"), # post_id에 대응하는 봉사에 신청하기위해 apply_main_sub로 이동
    path('apply_new/',views.apply_new, name="apply_new"), # db에 저장하기위해 views에 db에 저장하는 apply_new로 이동
    path('apply_result/<int:post_id>',views.apply_result, name="apply_result"), # 결과를 보기위해 views에 apply_result로 이동
  

]