from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignupForm(UserCreationForm):
    class  Meta:
        model = User
        fields =  ['username', 'email','password1', 'password2']
 
class UserForm(forms.ModelForm):
    pass
    class   Meta:
        db_table = ''
        model = User
        fields = ['first_name', 'last_name','email']
        
        
class ProfileForm(forms.ModelForm):
    class   Meta:
        db_table = ''
        model = Profile
        fields = ['address', 'image']
 