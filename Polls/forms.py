
from django import forms
from crispy_forms.helper import FormHelper
from . models import *


class CrudFrom(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title','Author','description','slug','image','Rewiew','genreTree') 

        widget = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'Author': forms.SelectMultiple(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'Rewiew':forms.ModelChoiceField(queryset=Book.objects.all()),
            'genreTree': forms.SelectMultiple(attrs={'class':'form-control'}),
        }


