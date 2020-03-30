from django.contrib import admin
from django.conf.urls import url
from .views import emailView, successView

urlpatterns = [
    url(r'^email/$', emailView, name='email'),
    url(r'^success/$', successView, name='success'),
]