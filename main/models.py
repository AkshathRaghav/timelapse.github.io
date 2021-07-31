from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class test(models.Model) : 
    name = models.CharField(max_length = 100)
    img = models.ImageField(upload_to = 'pics')

class events(models.Model)  : 
    username = models.CharField(max_length = 30)
    email = models.CharField(max_length=100)
    number =  models.CharField(max_length=20, default = "Not Added Yet")
    schoolname = models.CharField(max_length=150, default = "Not Added Yet")
    grade = models.IntegerField(null=True, default= 0)
    section = models.CharField(max_length=5, default="*")
    code = models.CharField(max_length=100, default = "*")
    e1 = models.CharField(max_length = 20)
    e2 = models.CharField(max_length = 20)
    e3 = models.CharField(max_length = 20)
