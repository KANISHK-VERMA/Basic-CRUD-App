from django import forms
from .models import Student

class Sform(forms.ModelForm):
    class Meta:
        model=Student
        fields=('name','rollnum','course')
