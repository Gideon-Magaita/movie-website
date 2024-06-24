from django.shortcuts import render,redirect

# Create your views here.


def home(request):
    return render(request,'pages/user/home.html')

def about(request):
    return render(request,'pages/user/about.html')

def review(request):
    return render(request,'pages/user/review.html')