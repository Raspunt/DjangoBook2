from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms



class SummerNoteForComment(forms.Form):
    text = forms.CharField(widget=SummernoteWidget(attrs={'name':'commentText'}))