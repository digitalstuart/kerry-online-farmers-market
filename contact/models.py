from django.db import models

class Contact(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    your_name = models.CharField(max_length=100, default='')