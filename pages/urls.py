from django.urls import path
from .views import privacy_policy

urlpatterns = [
    path('privacy_policy/', privacy_policy, name="privacy_policy")   
]