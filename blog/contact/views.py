from pickle import GET
from django.conf import settings
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


def contact_me(request):
    if request.method == 'GET':
        return render(request, 'contact/contact.html')
    else:
        form = ContactForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                email_subject = f'New email from: {form.cleaned_data["from_email"]}: {form.cleaned_data["subject"]}'
                email_message = form.cleaned_data['message']
                send_mail(email_subject, email_message,
                          settings.CONTACT_EMAIL, [settings.CONTACT_EMAIL])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'contact/success.html')
