def get_duration_matrix(client, locations):
    """
    Given a dictionary of locations, returns a matrix of walking durations between each location in minutes.
    
    :param client: The Google Maps client instance.
    :param locations: A dictionary where keys are location names and values are tuples of (latitude, longitude).
    :return: A matrix containing walking durations between each location (in minutes).
    """
    # Extracting the latitudes and longitudes from the dictionary
    origins = [location for location in locations.values()]
    n = len(origins)

    # Initialize the matrix to store durations in minutes
    duration_matrix_values = [[None] * n for _ in range(n)]

    # Function to fetch durations for a submatrix
    def fetch_submatrix(origins_subset, destinations_subset, start_row, start_col):
        distance_matrix = client.distance_matrix(origins_subset, destinations_subset, mode='walking')
        for i, row in enumerate(distance_matrix['rows']):
            for j, element in enumerate(row['elements']):
                if element['status'] == 'OK':
                    duration_matrix_values[start_row + i][start_col + j] = element['duration']['value'] / 60
                else:
                    duration_matrix_values[start_row + i][start_col + j] = None

    # Splitting the locations into chunks of up to 10
    chunk_size = 10
    for i in range(0, n, chunk_size):
        for j in range(0, n, chunk_size):
            origins_subset = origins[i:i + chunk_size]
            destinations_subset = origins[j:j + chunk_size]
            fetch_submatrix(origins_subset, destinations_subset, i, j)

    return duration_matrix_values

def main():
    load_dotenv()
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    gmaps = googlemaps.Client(key=api_key)
    
    # Example usage with the provided pub locations:
    locations = {
        "New Britannia": (-33.8885236, 151.1964246),
        "Hotel Regent Sydney": (-33.8923563, 151.2003466),
        "The Redfern": (-33.8927134, 151.2019184),
        "The Eveleigh Hotel": (-33.8894120, 151.1982250)
    }

    # Get the walking duration matrix in minutes
    duration_matrix = get_duration_matrix(gmaps, locations)

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
