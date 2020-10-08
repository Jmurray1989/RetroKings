from django.shortcuts import render, redirect, reverse
from .models import Contact
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail

import os
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')


def contact(request):
    """
    Renders contact form.

    """
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = Contact(
                name=request.POST.get('name'),
                message=request.POST.get('message'),
                email=request.POST.get('email'),
                user_id=request.user
            )
            form.save()
        else:
            form = Contact(
                name=request.POST.get('name'),
                message=request.POST.get('message'),
                email=request.POST.get('email'),
            )
            form.save()

        # Send Email to admin informing them they have a new message
        send_mail(
            'New Message Received',
            'Hi Admin,\n\nYou have a new message. Sign '
            'into the admin panel to view.\n\nRegards,'
            '\nRetroKings',
            'retrokingsinc@gmail.com',
            [EMAIL_HOST_USER],
            fail_silently=True
        )
        # Success message
        messages.success(request, 'Contact form successfully submitted. We will be in touch!')
        return redirect(reverse('contact_success'))

    context = {
        'form': ContactForm
    }
    return render(request, 'contact/contact.html', context)


# Contact success page
def contact_success(request):
    return render(request, "contact/contact_success.html")
