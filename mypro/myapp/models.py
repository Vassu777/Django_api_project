from django.db import models

# Create your models here.
class candidate(models.Model):
    username =models.CharField(max_length=100)
    email =models.CharField(max_length=200)
    mobile =models.CharField(max_length=15)
    pasword = models.CharField(max_length=20)
    confirm_pasword = models.CharField(max_length=20)