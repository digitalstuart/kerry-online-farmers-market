from django.conf.urls import url
from .views import all_products, add_or_edit_product, delete_product


urlpatterns = [
    url(r'^all/', all_products, name="products"),
    url(r'^new/$', add_or_edit_product, name="new_product"),
    url(r'^(?P<pk>\d+)/edit/$', add_or_edit_product, name="edit_product"),
    url(r'^(?P<pk>\d+)/delete/$', delete_product.as_view(), name="delete_product")
]