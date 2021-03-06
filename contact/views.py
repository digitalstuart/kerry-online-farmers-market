from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def emailView(request):
    """
    Renders the contact form page
    Checks for message being sent
    With reference to https://wsvincent.com/django-contact-form
    """
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            your_name = form.cleaned_data['your_name']
            try:
                send_mail(subject, message, your_name, ['stuandjordan@hotmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})


def successView(request):
    """Renders the message success page"""
    return render(request, "success.html")