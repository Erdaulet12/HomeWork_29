from django import forms
from .models import BBCodeEntry


class BBCodeForm(forms.ModelForm):
    class Meta:
        model = BBCodeEntry
        fields = ['title', 'bbcode_content']
        widgets = {
            'bbcode_content': forms.Textarea(attrs={'rows': 10, 'cols': 80, 'placeholder': 'Введите BBCode'}),
        }
