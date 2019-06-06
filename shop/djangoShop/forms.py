from .models import Order
from django import forms as forms_django


class OrderForm(forms_django.ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'city')