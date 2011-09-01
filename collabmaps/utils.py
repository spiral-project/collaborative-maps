import urllib
import json

def geocode(address):
    """Geocode an address using the google API"""
    address = urllib.quote_plus(address)
    url = "http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=%s" % address
    response = json.loads(urllib.urlopen(url).read())
    if response["status"] == "OK":
        latlong = response["results"][0]["geometry"]["location"]
        return latlong["lat"], latlong["lng"]
    else:
        raise Exception(response["status"])
