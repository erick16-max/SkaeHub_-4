#search the country name from a given state name using the Nominatim API and GeoPy package.

from geopy.geocoders import Nominatim

def find_country_name(state):
    geolocator = Nominatim(user_agent='geoapiExercises')

    location = geolocator.geocode(state)

    country_name = location.address
    return country_name


print(find_country_name('london'))