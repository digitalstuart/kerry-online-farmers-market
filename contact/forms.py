from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('your_name', 'subject', 'message')
        labels = {'message':'Message (please include your contact email address)'}