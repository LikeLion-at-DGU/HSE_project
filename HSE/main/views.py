from django.shortcuts import render

def showMain(request):
    return render(request,'main/index.html')

def componentsMain(request):
    return render(request, 'main/components.html')