#payments/urls.py
from django.urls import path
from .views import checkout,charge

urlpatterns = [
    path('checkout', checkout.as_view(), name="checkout"),
    path('charge',charge,name='charge'),
]
