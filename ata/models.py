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
