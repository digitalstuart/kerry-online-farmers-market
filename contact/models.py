from django.db import models

class Contact(models.Model):
    from_email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return "{0} {1} {2}".format(
            self.from_email, self.subject, self.message)
