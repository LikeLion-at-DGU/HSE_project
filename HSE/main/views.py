from django.shortcuts import render

def showMain(request):
    return render(request,'main/index.html')

