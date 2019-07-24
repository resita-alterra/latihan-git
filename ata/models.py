from django.db import models

# Create your models here.
class Mentee(models.Model):
    nama = models.CharField(max_length=255)
    quotes = models.CharField(max_length=255)
    profile_pic = models.CharField(max_length=255)