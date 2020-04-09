from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to='images')  
    ingredients = models.TextField()
    method = models.TextField()

    def __str__(self):
        return self.name