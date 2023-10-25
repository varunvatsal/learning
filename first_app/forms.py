from dataclasses import field
from tkinter.ttk import Style
from django import forms 
from .models import course
from django.forms import ModelForm 


class CourseForm(ModelForm):
    class Meta:
        model = course
        fields = "__all__"  
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'year': forms.NumberInput(attrs={'class':'form-control'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'course_name': forms.TextInput(attrs={'class':'form-control'}),
            'course_desc': forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
        }
