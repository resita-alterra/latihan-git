from django import forms
from .models import Mentee

class MenteeForm(forms.ModelForm):
    
    class Meta:
        model = Mentee
        fields = ('nama', 'quotes', 'profile_pic')