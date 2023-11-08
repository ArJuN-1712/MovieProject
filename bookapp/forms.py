from django import forms
from . models import Book

class Booklist(forms.ModelForm):
    class Meta:
        model=Book
        fields=['name','desc','author','img']
