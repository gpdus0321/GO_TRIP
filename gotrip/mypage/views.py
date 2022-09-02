from django.shortcuts import render, get_object_or_404


# Create your views here.
from blogapp.models import Post


def mypage(request):
    return render(request, 'mypage.html', )
