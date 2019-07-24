from django.shortcuts import render
from .models import Mentee, Mentor
from .forms import MenteeForm

# Create your views here.
def mentee(request):
    murid = Mentee.objects.all
    return render(request, 'mentee.html', {'murid':murid})
# Create your views here.

def mentor(request):
    mentor = Mentor.objects.all()
    return render(request, 'mentor.html', {'mentor' : mentor})

