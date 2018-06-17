from django import forms
from django.forms import ModelForm
from .models import Info

class InfoForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name...'}))

    class Meta:
        model = Info
        fields = '__all__'
