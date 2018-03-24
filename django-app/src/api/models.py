from django.db import models

from django.contrib.gis.db import models as gis_models
from localflavor.us.models import USStateField


class Business(models.Model): 
    name = models.CharField(max_length=255, blank=False)
    address_1 = models.CharField(max_length=255, blank=True)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state = USStateField(blank=True)
    zipcode = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)

    geolocation = gis_models.PointField(blank=True, null=True)

    class Meta:
        unique_together = (('name', 'address_1'),)

    def __str__(self):
        return self.name


class Happyhour(models.Model):
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    well_price = models.CharField(max_length=255, blank=True)
    draft_price = models.CharField(max_length=255, blank=True)
    business = models.ForeignKey(
        'Business',
        on_delete=models.CASCADE,
        blank=False,
        )

