from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField()
    quantity = forms.CharField()
