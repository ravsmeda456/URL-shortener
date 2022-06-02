from logging import PlaceHolder
from django import forms

class urlForm(forms.Form):
    actual_url = forms.CharField(label='Enter the URL...', 
                                widget=forms.TextInput(attrs={'placeholder': 'Enter the url'}),
                                max_length=200,
                                )
