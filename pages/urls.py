from django.urls import path
from .views import privacy_policy, faq, tandc

urlpatterns = [
    path('privacy_policy/', privacy_policy, name="privacy_policy"),
    path('faq/', faq, name="faq"),
    path('tandc/', tandc, name="tandc"),
]
