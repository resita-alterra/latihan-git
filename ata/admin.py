from django.contrib import admin
from .models import Mentor

class MentorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'exp', 'quote','url_file_image']
    ordering = ['id']

admin.site.register(Mentor, MentorAdmin)
# Register your models here.
