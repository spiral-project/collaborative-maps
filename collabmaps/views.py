from datetime import datetime
from django.shortcuts import render_to_response
from django.db.models import Q

from .models import Event, Place

def display_map(request):
    """Return the places registered in the system that are either 
    static places or upcoming events.
    """

    # Concatenate the places and events as lists
    places = list(Place.objects.all())

    # events can be started and not yet finished
    places.extend(list(Event.objects.filter(
            Q(start_date__gt=datetime.now()) | Q(stop_date__gt=datetime.now())
    )))
    return render_to_response('display_map.html', {'places': places})
