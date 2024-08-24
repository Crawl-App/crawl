import googlemaps
import os
from dotenv import load_dotenv

# Initialise client based off API key in environment variables
load_dotenv()
api_key = os.getenv('GOOGLE_MAPS_API_KEY')
gmaps = googlemaps.Client(key=api_key)

# Define the location (latitude, longitude) and the search parameters
def get_nearby(coordinates, place_type):
    """
    Gets the nearby 'place's based on the given coordinates.
      - coordinates: a tuple of float coordinates
      - place_type: a relevant search term for what the user wishes to do.
    """
    radius = 5000  # Radius in meters # TODO: Should this always be constant or be configurable?
    
    # Perform the Places API nearby search request
    places_result = gmaps.places_nearby(location=coordinates, radius=radius, keyword=place_type)

    # Extract the results
    # TODO: Make me asynchronous
    return places_result.get('results', [])

"""
# test
places = get_nearby((-33.88928457080163, 151.19347275195244), 'pub')


# Print details of each place found
for place in places:
    if place.get('rating'):
        rating = place.get('rating')
        name = place.get('name')
        address = place.get('vicinity')
        price_level = ('$'*place.get('price_level') if place.get('price_level') else 'None')
        print(f"Name: {name}, Address: {address}, \
            Rating: {rating} from {place.get('user_ratings_total')} reviews. \
            Price level = {price_level}\n")    
"""        

# use Distance Matrix API for possible distances -> one request then 'cache' response to access in algo

