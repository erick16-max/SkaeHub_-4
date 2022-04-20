#write a Python program to find the details of a given zip code using the
from geopy.geocoders import Nominatim

def get_address(zip_code):
    geolocator = Nominatim(user_agent="geoapiExcersices")

    location = geolocator.geocode(zip_code)

    address = location.address
    return address

print(get_address(80401))