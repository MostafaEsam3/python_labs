from django import forms
from author.models import*
from .models import *
class Addbook(forms.Form):
    title=forms.CharField(required=True,max_length=200)
    version=forms.NumberInput()
    author=forms.ChoiceField(choices=Author.get_all())
class addBookModel(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'