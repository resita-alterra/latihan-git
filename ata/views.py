from django.shortcuts import render
from .models import Mentee
from .forms import MenteeForm

# Create your views here.
def mentee(request):
    murid = Mentee.objects.all
    return render(request, 'mentee.html', {'murid':murid})