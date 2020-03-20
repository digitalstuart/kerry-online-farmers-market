from django.conf.urls import url, include
from .views import all_products, ProductCreate, ProductDelete, ProductUpdate

urlpatterns = [
    url(r'^all/', all_products, name="products"),
    url(r'^add_product/', ProductCreate.as_view(), name="create"),
    url(r'^edit_product/', ProductUpdate.as_view(), name="update"),
    url(r'^delete_product/', ProductDelete.as_view(), name="delete"),    
]