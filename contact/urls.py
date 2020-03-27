from django.conf.urls import url
from .views import email, thanks

urlpatterns = [
    url(r'^email/$', email, name='email'),
    url(r'^thanks/$', thanks, name='thanks'),
]