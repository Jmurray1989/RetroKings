from django.shortcuts import render, redirect, reverse
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail

import os
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')


def contact(request):
    """
    Renders contact template and contact
    form.
    """
    if request.method == 'POST':
        if request.user.is_authenticated:
            create_contact_form = Contact(
                name=request.POST.get('name'),
                message=request.POST.get('message'),
                email=request.POST.get('email'),
                user_id=request.user
            )
            create_contact_form.save()
        else:
            create_contact_form = Contact(
                name=request.POST.get('name'),
                message=request.POST.get('message'),
                email=request.POST.get('email'),
            )
            create_contact_form.save()

    context = {
        'form': ContactForm
    }
    return render(request, 'contact/contact.html', context)
