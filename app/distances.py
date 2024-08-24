import googlemaps
import os
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
api_key = os.getenv('GOOGLE_MAPS_API_KEY')
gmaps = googlemaps.Client(key=api_key)

def get_walking_duration_matrix_in_minutes(locations):
    """
    Given a dictionary of locations, returns a matrix of walking durations between each location in minutes.
    
    :param locations: A dictionary where keys are location names and values are tuples of (latitude, longitude).
    :return: A matrix containing walking durations between each location (in minutes).
    """
    # Extracting the latitudes and longitudes from the dictionary
    origins = [location for location in locations.values()]
    destinations = origins.copy()  # In this case, destinations are the same as origins

    # Perform the distance matrix request with walking mode
    distance_matrix = gmaps.distance_matrix(origins, destinations, mode='walking')

    # Initialize the matrix to store durations in minutes
    duration_matrix_values = []

    for row in distance_matrix['rows']:
        durations = []
        for element in row['elements']:
            if element['status'] == 'OK':
                durations.append(element['duration']['value'] / 60)  # Convert duration to minutes
            else:
                durations.append(None)
        duration_matrix_values.append(durations)

    return duration_matrix_values

def main():
    # Example usage with the provided pub locations:
    locations = {
        "New Britannia": (-33.8885236, 151.1964246),
        "Hotel Regent Sydney": (-33.8923563, 151.2003466),
        "The Redfern": (-33.8927134, 151.2019184),
        "The Eveleigh Hotel": (-33.8894120, 151.1982250)
    }

    # Get the walking duration matrix in minutes
    duration_matrix = get_walking_duration_matrix_in_minutes(locations)

    # Print the results
    print("Walking Duration Matrix (minutes):")
    pub_names = list(locations.keys())

    # Print the header row
    print(f"{' ':<20}", end="")
    for name in pub_names:
        print(f"{name:<20}", end="")
    print()

    # Print each row of the matrix with labels
    for i, row in enumerate(duration_matrix):
        print(f"{pub_names[i]:<20}", end="")
        for duration in row:
            if duration is not None:
                print(f"{duration:<20.2f}", end="")
            else:
                print(f"{'N/A':<20}", end="")
        print()

if __name__ == "__main__":
    main()
