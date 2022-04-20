#get the city, state and country name of a specified latitude and longitude using Nominatim API and Geopy package.


from geopy.geocoders import Nominatim

def get_city_state_country(latitude, longitude):

    geolocator = Nominatim(user_agent="geoapiExcercise")

    location = geolocator.reverse((latitude, longitude), exactly_one=True)

    address = location.raw['address']
    city = address['city']
    state = address['state']
    country = address['country']

    return city, state, country