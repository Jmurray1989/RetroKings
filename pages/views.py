from django.shortcuts import render


def privacy_policy(request):
    """
    Renders view for the privacy policy page
    """
    return render(request, "privacy_policy.html")


def faq(request):
    """
    Renders view for the terms and conditions page
    """
    return render(request, "faq.html")
