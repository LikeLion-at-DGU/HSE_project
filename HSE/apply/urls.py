from django.urls import path
from . import views

app_name = "apply"
urlpatterns = [
   

    path('apply_main_sub/<int:post_id>',views.apply_main_sub, name="apply_main_sub"),
    path('apply_new/',views.apply_new, name="apply_new"),
    path('apply_result/<int:post_id>',views.apply_result, name="apply_result"),
    

]