from django import forms
from .models import WikiPage

class wikiPageForm(forms.ModelForm):
    class Meta:
        model = WikiPage
        fields = ['title', 'content']