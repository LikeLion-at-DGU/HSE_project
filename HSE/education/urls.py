from django.urls import path
from .views import *

app_name = "education"

urlpatterns = [
    path("<int:id>/", detail, name="detail"),  # 글 상세 페이지
    path("new/", new, name="new"),  # 새 글 작성 페이지
    path("create/", create, name="create"),  # 새 글 작성 동작
    path("edit/<int:id>", edit, name="edit"),  # 기존 글 수정 페이지
    path("update/<int:id>", update, name="update"),  # 기존 글 수정 동작
    path("delete/<int:id>", delete, name="delete"),  # 기존 글 삭제
    path("", edulist, name="edulist"),  # 글 목록 페이지
]