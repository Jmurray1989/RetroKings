from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """ Contact form """
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'message'
        ]

    name = forms.CharField(
        required=True,
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control-contact',
            'placeholder': 'Your name'
        })
    )
    message = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control-contact',
            'placeholder': 'Your message'
        })
    )
    email = forms.EmailField(
        required=True,
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control-contact',
            'placeholder': 'Your email'
        })
    )
