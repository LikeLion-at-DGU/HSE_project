from django.shortcuts import render, redirect, get_object_or_404
from .models import EduPost
from apply.models import apply
from django.utils import timezone
import datetime

# Create your views here.

# 봉사활동 게시글 목록 보여주는 페이지
def edulist(request):
    post = EduPost.objects.all()
    post = post.order_by("-pub_date")
    return render(request, "education/edulist.html", {"posts": post})


# 봉사활동 게시글 상세 페이지
def detail(request, id):
    post = get_object_or_404(EduPost, pk=id)
    # author: 현재 유저가 게시글 작성자와 동일한지 전달하는 변수 (이후 수정하기, 삭제하기 버튼 띄울지 말지 결정)
    if request.user == post.writer:
        author = True
    else:
        author = False
    # cmp에 현재 시간 받아와서 저장하고 형식 맞춘 후 pub_date와 비교하여 마감됐는지 확인하고 저장
    cmp = datetime.datetime.now()
    cmp = cmp.strftime("%y-%m-%d %H:%M:%S")
    cmp = datetime.datetime.strptime(cmp, "%y-%m-%d %H:%M:%S")
    if post.due_date >= cmp:
        is_dead = True
    else:
        is_dead = False
    # 봉사 게시글 정보, 글 작성자 여부, 봉사 마감 여부 전달
    return render(
        request,
        "education/detail.html",
        {"post": post, "author": author, "is_dead": is_dead},
    )


# 새 글 작성 페이지
def new(request):
    return render(request, "education/new.html")


# 새 글 작성 동작
def create(request):
    # 모델 설명과 동일
    new_post = EduPost()
    new_post.title = request.POST["title"]
    new_post.writer = request.user  # 현재 접속한 유저를 글 작성자로
    new_post.pub_date = timezone.now()  # 현재 시간을 게시글 작성 시간으로
    new_post.due_date = request.POST["due_date"]
    new_post.work_date = request.POST["work_date"]
    new_post.main_teacher = request.POST["main_teacher"]
    new_post.sub_teacher = request.POST["sub_teacher"]
    new_post.work_hour = request.POST["work_hour"]
    new_post.body = request.POST["body"]
    # 입력한 유튜브 동영상 주소에서 필요없는 부분 제하고 iframe 형식 맞추기 (& 뒤에 재생시간 정보가 있어서 제거)
    new_post.video = request.POST["video"].replace("watch?v=", "embed/")
    if "&" in new_post.video:
        new_post.video = new_post.video[: new_post.video.index("&")]
    new_post.extrafile = request.FILES.get("extrafile")
    new_post.image = request.FILES.get("image")
    new_post.save()

    return redirect("education:detail", new_post.id)


# 기존 봉사 게시글 수정 페이지
def edit(request, id):
    edit_post = EduPost.objects.get(id=id)
    # author : 현재 접속한 유저가 수정하려는 게시글의 작성자인지 확인하고 저장
    if request.user == edit_post.writer:
        author = True
    else:
        author = False
    return render(request, "education/edit.html", {"post": edit_post, "author": author})


# 기존 봉사 게시글 수정 동작
def update(request, id):
    ap_all = apply.objects.all()
    update_post = EduPost.objects.get(id=id)
    update_post.title = request.POST["title"]
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.due_date = request.POST["due_date"]
    update_post.main_teacher = request.POST["main_teacher"]
    update_post.sub_teacher = request.POST["sub_teacher"]
    update_post.work_hour = request.POST["work_hour"]
    update_post.body = request.POST["body"]
    update_post.video = request.POST["video"].replace("watch?v=", "embed/")
    if "&" in update_post.video:
        update_post.video = update_post.video[: update_post.video.index("&")]
    update_post.extrafile = request.FILES.get("extrafile")
    update_post.image = request.FILES.get("image")
    update_post.count = 0
    for i in ap_all:
        if i.title == update_post.title:
            i.winner = ""
            i.save()
    update_post.save()

    return redirect("education:detail", update_post.id)


# 봉사 게시글 삭제
def delete(request, id):
    delete_post = EduPost.objects.get(id=id)
    delete_post.delete()

    return redirect("education:edulist")