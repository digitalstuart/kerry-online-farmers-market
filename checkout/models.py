from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    name = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=25, blank=False)
    email_address = models.EmailField(blank=False)
    address_line_1 = models.CharField(max_length=50, blank=False)
    address_line_2 = models.CharField(max_length=50, blank=False)
    town = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=50, blank=False)
    eircode = models.CharField(max_length=20, blank=True)
    date = models.DateField()
    user = models.ForeignKey(User)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.name)


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, related_name='orders')
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)
    user = models.ForeignKey(User, blank=False, related_name="products")

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price)