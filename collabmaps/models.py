from django.db import models

class Location(models.Model):
    """Represent a point, a location. The model contains information about
    the name of the location as well as the latitude and longitude"""
    pass

class Event(models.Model):
    """Represents an event, containing a start date, a stop date and a location"""

    name = models.TextField()
    description = models.TextField(blank=True)
    website = models.URLField(verify_exists=Falsex, blank=True)
    location = models.ForeignKey(Location, related_name='event')
    start_date = models.DateField(blank=False)
    stop_date = models.DateField(blank=True)

class Place(models.Model):
    """A place, with a name and a location, + description"""
    name = models.TextField()
    description = models.TextField(blank=True)
    website = models.URLField(verify_exists=Falsex, blank=True)
    location = models.ForeignKey(Location, related_name='event')
