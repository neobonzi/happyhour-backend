from django.db import models


class Business(models.Model): 
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.question