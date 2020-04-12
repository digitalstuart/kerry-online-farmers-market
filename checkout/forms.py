from django import forms
from .models import Order


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2020, 2036)]

    credit_card_number = forms.CharField(label='Card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False, help_text='Last 3 numbers on back of card')
    expiry_month = forms.ChoiceField(label='Expiry month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label='Expiry year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'name', 'phone_number', 'email_address', 'address_line_1',
            'address_line_2', 'town', 'county', 'eircode'
        )