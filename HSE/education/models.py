from django.db import models
from django.db.models.aggregates import Max
from django.contrib.auth.models import User

# Create your models here.
class EduPost(models.Model):
    title = models.CharField(max_length=200)  # 봉사활동 이름
    writer = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성자, User 모델 사용
    pub_date = models.DateTimeField()  # 글 최초 작성 일자
    due_date = models.DateTimeField()  # 봉사활동 마감 일자
    work_date = models.DateTimeField(null=True)  # 봉사활동 예정 일자(실제 봉사 하는 날)
    main_teacher = models.IntegerField()  # 모집하는 주 강사 수
    sub_teacher = models.IntegerField()  # 모집하는 보조 강사 수
    work_hour = models.IntegerField()  # 봉사활동 인정 시간(0도 가능)
    body = models.TextField()  # 봉사활동 관련 설명 본문
    video = models.CharField(null=True, max_length=200)  # 유튜브에 업로드한 동영상 url
    image = models.FileField(
        upload_to="image/", null=True
    )  # 봉사활동 관련 이미지(있으면 글 썸네일, 없으면 메인 로고가 글 썸네일)
    extrafile = models.FileField(
        upload_to="extrafiles/", null=True
    )  # 추가적으로 필요한 파일(봉사활동 관련 pdf 등)
    count = models.IntegerField(default=0)  # 각 봉사당 결과가 한번만 랜덤으로 선정되게 count 값을 통해 확인
    """ count 만들기 전 봉사자로 선정된 결과를 확인할 때마다 랜덤으로 봉사자 중 뽑게돼서 
    이를 막기 위해 count = 0일 때만 봉사자를 뽑고 그 이후로 결과 확인을 해도 뽑힌 봉사자가 변하지 않도록 설정"""
