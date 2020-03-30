from django.conf.urls import url
from .views import all_sellers


urlpatterns = [
    url(r'^$', all_sellers, name="sellers")
]