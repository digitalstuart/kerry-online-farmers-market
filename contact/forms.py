from django import forms
from django.forms import ModelForm
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
        labels = {'message':'Message (please include your name and contact email address)'}