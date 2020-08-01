from django import forms
from .models import Application
from django.contrib.auth import get_user_model

class ApplicationForm(forms.ModelForm):
    class Meta():
        model=Application
        fields=('name','branch','schId','reason','explain','start_date','end_date','document')
        widget={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'branch':forms.TextInput(attrs={'class':'form-control'}),
            'schId':forms.TextInput(attrs={'class':'form-control'}),
            'reason':forms.Select(attrs={'class':'form-control'}),
            'explain':forms.Textarea(attrs={'class':'form-control'}),
            'start_date':forms.TextInput(attrs={'class':'form-control'}),
            'end_date':forms.TextInput(attrs={'class':'form-control'}),
            'document':forms.TextInput(attrs={'class':'form-control'}),
            
        }
        
class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model=get_user_model()
        fields=('schId','name','branch','email','password1','password2')
        
   

        