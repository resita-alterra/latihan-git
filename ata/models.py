from django.db import models

# Create your models here.
class Mentor(models.Model):
    nama = models.CharField(max_length=255)
    exp = models.CharField(max_length=255)
    quote = models.TextField()
    url_file_image = models.CharField(max_length=255)