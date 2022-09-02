from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages, auth
from django.contrib.auth import login, authenticate

# Create your views here.
from blogapp.models import Post

from .forms import CreateForm
from .models import CreateAccount


def intro(request):
    return render(request, 'serviceapp/intro.html')


def main(request):
    nac_rank = Post.objects.filter().order_by('-counting')
    nac_rank = nac_rank[:3]
    return render(request, 'serviceapp/main.html', {'nac_rank':nac_rank})


def course(request):
    return render(request, 'serviceapp/course.html')

def login(request):
    return render(request, 'serviceapp/login.html')


def membership(request):
    return render(request, 'serviceapp/membership.html')


def write(request):
    return render(request, 'serviceapp/write.html')

def create(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'serviceapp/create.html')
    return render(request, 'serviceapp/create.html')





