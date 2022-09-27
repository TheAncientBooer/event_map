from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=False)
    location = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()

    def __str__(self):
        return self.text[:50]