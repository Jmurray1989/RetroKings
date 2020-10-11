from django.shortcuts import render


def privacy_policy(request):
    """
    Renders view for the privacy policy page
    """
    return render(request, "privacy_policy.html")


def faq(request):
    """
    Renders view for the faq page
    """
    return render(request, "faq.html")


def tandc(request):
    """
    Renders view for the terms & conditions page
    """
    return render(request, "tandc.html")
