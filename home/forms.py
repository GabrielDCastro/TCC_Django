from django import forms

class Contact(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Dúvida', widget=forms.Textarea)