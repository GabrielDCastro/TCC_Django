from django import forms
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect


class Contact(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Dúvida', widget=forms.Textarea)

    def send_email(request):
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('from_email', '')
        if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact/thanks/')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')
