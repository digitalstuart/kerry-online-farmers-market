from django import forms
from .forms import Seller

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('name', 'address', 'email', 'phone', 'items')
