from django.shortcuts import render, redirect, get_object_or_404
from .models import EduPost
from django.utils import timezone

# Create your views here.


def detail(request, id):
    post = get_object_or_404(EduPost, pk=id)
    return render(request, "education/detail.html", {"post": post})


def new(request):
    return render(request, "education/new.html")


def create(request):
    new_post = EduPost()
    new_post.title = request.POST["title"]
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.due_date = request.POST["due_date"]
    new_post.main_teacher = request.POST["main_teacher"]
    new_post.sub_teacher = request.POST["sub_teacher"]
    new_post.body = request.POST["body"]
    new_post.video = request.FILES.get("video")
    new_post.extrafile = request.POST["extrafile"]
    new_post.save()
    return redirect("education:detail", new_post.id)


def edit(request, id):
    edit_post = EduPost.objects.get(id=id)
    return render(request, "education/edit.html", {"post": edit_post})


def update(request, id):
    update_post = EduPost.objects.get(id=id)
    update_post.title = request.POST["title"]
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.due_date = request.POST["due_date"]
    update_post.main_teacher = request.POST["main_teacher"]
    update_post.sub_teacher = request.POST["sub_teacher"]
    update_post.body = request.POST["body"]
    update_post.video = request.FILES.get("video")
    update_post.extrafile = request.POST["extrafile"]
    update_post.save()
    return redirect("education:detail", update_post.id)


def delete(request, id):
    delete_post = EduPost.objects.get(id=id)
    delete_post.delete()
    return redirect("main:mainpage")