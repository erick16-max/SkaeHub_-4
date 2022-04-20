#Python program to calculate the distance between Cairo and Nairobi City
from geopy.geocoders import Nominatim
from geopy import distance

city_one = 'Cairo'
city_two = 'Nairobi'

def get_distance_btwn_cities(city_one, city_two):
    geolocator = Nominatim(user_agent="geoapiExercises")

    l1 = geolocator.geocode(city_one)
    l2 = geolocator.geocode(city_two)

    location_one = ((l1.latitude, l2.longitude))
    location_two = ((l2.latitude, l2.longitude))

    distance_btwn_cairo_nairobi = distance.distance(location_one, location_two).km, "kilometres"

    return distance_btwn_cairo_nairobi

print(get_distance_btwn_cities(city_one, city_two))