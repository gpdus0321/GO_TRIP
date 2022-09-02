from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from .views import mypage

app_name = "mypage"

urlpatterns = [
    path('', mypage, name='mypage'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)