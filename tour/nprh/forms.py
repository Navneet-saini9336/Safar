from django import forms
from .models import(demotable)

class demoforms(forms.ModelForm):
    class Meta:
        model = demotable

        fields = [
            "title",
            "description", 
        ]