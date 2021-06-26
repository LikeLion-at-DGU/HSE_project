from django.urls import path
from . import views

app_name = "apply"
urlpatterns = [
   
    path('apply_detail/<int:id>',views.apply_detail, name="apply_detail"),
    path('apply_main/',views.apply_main, name="apply_main"),
    path('apply_sub/',views.apply_sub, name="apply_sub"),
    path('apply_new/',views.apply_new, name="apply_new"),
    path('apply_result/<int:id>',views.apply_result, name="apply_result"),
]