from django.shortcuts import render
from .models import Mentee, Mentor, Blog
from .forms import MenteeForm

def mentee(request):
    murid = Mentee.objects.all
    return render(request, 'mentee.html', {'murid':murid})
# Create your views here.

def mentor(request):
    mentor = Mentor.objects.all()
    return render(request, 'mentor.html', {'mentor' : mentor})

def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', {'blog': blog})


