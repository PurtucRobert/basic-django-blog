from pickle import GET
from django.shortcuts import render
from .forms import ContactForm


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
            return render(request, 'contact/success.html')
