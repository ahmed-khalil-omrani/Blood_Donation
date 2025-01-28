from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import BloodDonor , BloodNeeder
class UserForm(UserCreationForm):
    class Meta:
        model=User 
        fields=['username','email','password1','password2']
class DonorForm(forms.ModelForm):
    class Meta:
        model=BloodDonor 
        fields=['first_name','last_name','birth_day','blood_type']
class NeederForm(forms.ModelForm):
    class Meta:
        model=BloodNeeder
        fields=['first_name','last_name','birth_day','blood_type']

