from django import  forms
from .models import Apply,Job



class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields =['name', 'email','website','cover_letter','cv']   

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields ='__all__'
        exclude=['slug','owner']