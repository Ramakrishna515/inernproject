from django import forms
from .models import buyer


class Newuser(forms.ModelForm):
    class Meta():
        model=buyer
        fields='__all__'