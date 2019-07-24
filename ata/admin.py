from django.contrib import admin
from .models import Mentee, Mentor

class MentorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'exp', 'quote','url_file_image']
    ordering = ['id']

admin.site.register(Mentor, MentorAdmin)
# Register your models here.

admin.site.register(Mentee)