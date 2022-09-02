from django.db import models

# Create your models here.
class Post(models.Model):
  image = models.ImageField(upload_to = "images/", null=True, blank=True)

  def __str__(self):
    return str(self.title)

class CreateAccount(models.Model):
  username = models.CharField(max_length=10, null=False, primary_key=True)
  password1 = models.CharField(max_length=20, null=False)
  password2 = models.CharField(max_length=20, null=False)
