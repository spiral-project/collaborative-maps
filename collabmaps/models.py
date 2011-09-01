from django.db import models
from .utils import geocode

class BasePlace(models.Model):
    """Represent a point, a location. The model contains information about
    the name of the location as well as the latitude and longitude"""
    name = models.TextField()
    description = models.TextField(blank=True)
    website = models.URLField(verify_exists=False, blank=True)
    address = models.CharField(max_length=400)
    latitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)

    def save(self):
        """Geocode on save"""
        if not self.latitude or not self.longitude: #FIXME update ?
            self.latitude, self.longitude = geocode(self.address)
        super(BasePlace, self).save()

    @property
    def is_event(self):
        return False

    class Meta:
        abstract = True

class Event(BasePlace):
    start_date = models.DateField(blank=False)
    stop_date = models.DateField(blank=True, null=True)

    @property
    def is_event(self):
        return True

class Place(BasePlace):
    pass
