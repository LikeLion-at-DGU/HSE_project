from django.shortcuts import render, redirect, get_object_or_404
from .models import EduPost
from apply.models import apply
from django.utils import timezone
import datetime

# Create your views here.


def edulist(request):
    post = EduPost.objects.all()
    post = post.order_by("-pub_date")
    return render(request, "education/edulist.html", {"posts": post})


def detail(request, id):
    post = get_object_or_404(EduPost, pk=id)

    if request.user == post.writer:
        author = True
    else:
        author = False

    cmp = datetime.datetime.now()
    cmp = cmp.strftime("%y-%m-%d %H:%M:%S")
    cmp = datetime.datetime.strptime(cmp, "%y-%m-%d %H:%M:%S")
    if post.due_date >= cmp:
        is_dead = True
    else:
        is_dead = False

    return render(
        request,
        "education/detail.html",
        {"post": post, "author": author, "is_dead": is_dead},
    )


def new(request):
    return render(request, "education/new.html")


def create(request):
    new_post = EduPost()
    new_post.title = request.POST["title"]
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.due_date = request.POST["due_date"]
    new_post.work_date = request.POST["work_date"]
    new_post.main_teacher = request.POST["main_teacher"]
    new_post.sub_teacher = request.POST["sub_teacher"]
    new_post.work_hour = request.POST["work_hour"]
    new_post.body = request.POST["body"]
    new_post.video = request.FILES.get("video")
    new_post.extrafile = request.FILES.get("extrafile")
    new_post.save()
    
    return redirect("education:detail", new_post.id)


def edit(request, id):
    edit_post = EduPost.objects.get(id=id)

    if request.user == edit_post.writer:
        author = True
    else:
        author = False
    return render(request, "education/edit.html", {"post": edit_post, "author": author})


def update(request, id):
    ap_all=apply.objects.all()
    update_post = EduPost.objects.get(id=id)
    update_post.title = request.POST["title"]
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.due_date = request.POST["due_date"]
    update_post.main_teacher = request.POST["main_teacher"]
    update_post.sub_teacher = request.POST["sub_teacher"]
    update_post.work_hour = request.POST["work_hour"]
    update_post.body = request.POST["body"]
    update_post.video = request.FILES.get("video")
    update_post.extrafile = request.FILES.get("extrafile")
    update_post.count=0
    for i in ap_all:
        if i.title == update_post.title:
            i.winner=''
            i.save()
    update_post.save()
    
    
    return redirect("education:detail", update_post.id)


def delete(request, id):
    delete_post = EduPost.objects.get(id=id)
    delete_post.delete()

    return redirect("education:edulist")