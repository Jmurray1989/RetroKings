from django.shortcuts import render


def privacy_policy(request):
    """
    Renders view for the privacy policy page
    """
    return render(request, "privacy_policy.html")
