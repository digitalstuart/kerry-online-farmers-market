from django.db import models

class Contact(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField()
    from_email = models.EmailField()

    def __str__(self):
        return "{0} {1} {2}".format(
            self.subject, self.message, self.from_email)
