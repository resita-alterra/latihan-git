from django.db import models

# Create your models here.

class Blog(models.Model):
    judul = models.CharField(max_length=255)
    gambar = models.CharField(max_length=100)
    tanggal = models.DateField()
    comment_cnt = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.judul

class Mentee(models.Model):
    nama = models.CharField(max_length=255)
    quotes = models.CharField(max_length=255)
    profile_pic = models.CharField(max_length=255)

class Mentor(models.Model):
    nama = models.CharField(max_length=255)
    exp = models.CharField(max_length=255)
    quote = models.TextField()
    url_file_image = models.CharField(max_length=255)
