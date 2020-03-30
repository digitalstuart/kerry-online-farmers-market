from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=254, default='')
    address = models.TextField()
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=254, default='')
    items = models.TextField()

    def __str__(self):
        return self.name