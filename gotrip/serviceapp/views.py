from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def intro(request):
    return render(request, 'serviceapp/intro.html')


def main(request):
    return render(request, 'serviceapp/main.html')


def course(request):
    return render(request, 'serviceapp/course.html')


def login(request):
    return render(request, 'serviceapp/login.html')


def membership(request):
    return render(request, 'serviceapp/membership.html')


def write(request):
    return render(request, 'serviceapp/write.html')
