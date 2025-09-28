from geopy.geocoders import Nominatim

# Initialize Nominatim geocoder
geolocator = Nominatim(user_agent="my-app-name") # Replace with a unique app name

# Geocode an address
location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
print(f"Address: {location.address}")
print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")

# Reverse geocode coordinates
coordinates = "37.4220, -122.0841"
location = geolocator.reverse(coordinates)
print(f"Address: {location.address}")