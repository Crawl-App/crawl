import googlemaps
from dotenv import load_dotenv
import os

# Load the API key from .env file
load_dotenv()
api_key = os.getenv('GOOGLE_MAPS_API_KEY')

# Initialize the Google Maps client
gmaps = googlemaps.Client(key=api_key)

# Use the IP address to get geolocation data (this part depends on what exactly you want to achieve)
location = gmaps.geolocate()

print("Location data:", location)
