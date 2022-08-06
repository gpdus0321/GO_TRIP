from django.db import models
from django.urls import reverse


class Post(models.Model):
    제목 = models.CharField(max_length=200)
    체크리스트1 = models.CharField(max_length=100, default='')
    체크리스트2 = models.CharField(max_length=100, default='')
    체크리스트3 = models.CharField(max_length=100, default='')
    이미지 = models.ImageField(blank=False, upload_to='blog_photo')
    내용 = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    counting = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.제목
