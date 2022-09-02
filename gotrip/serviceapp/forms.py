from django import forms
from .models import CreateAccount
from django_summernote.widgets import SummernoteWidget

class CreateForm(forms.ModelForm):
    class Meta:
        model = CreateAccount
        fields = ['username', 'password1', 'password2']