from django.conf.urls import url
from .views import all_sellers, add_seller


urlpatterns = [
    url(r'^$', all_sellers, name="sellers"),
    url(r'^new/$', add_seller, name="new_seller"),
]