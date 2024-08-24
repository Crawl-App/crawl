import heapq

def a_star(places, dist_matrix, num_stops):
    """
    Runs the A* algorithm on the set places, using distances from dist_matrix. Searches
    for a path of length num_stops however does not specify an end destination. Note
    the assumption is made that the indices of the places list corresponds to the row 
    and column indices of dist_matrix.
        - places: a list of place dictionaries, with at least name, location and rating
        - dist_matrix: a matrix of distances between the places in the list
        - num_stops: an integer representing the number of stops intended in the crawl.
    """
    start = 0  # Start from the first pub (index 0)
    queue = []
    heapq.heappush(queue, (0, start, [start]))  # (cost, current_pub, path)

    while queue:
        cost, current_pub, path = heapq.heappop(queue)

        # Check if the path contains the required number of stops. If so, stop.
        if len(path) == num_stops:
            return path, cost

        for next_pub in range(len(places)):
            if next_pub not in path:
                next_cost = cost + dist_matrix[current_pub][next_pub]
                heuristic = 1 / places[next_pub]['rating']  # Lower rating gives higher heuristic cost
                total_cost = next_cost + heuristic
                heapq.heappush(queue, (total_cost, next_pub, path + [next_pub]))

    return None, None

"""
# example pubs
places = [
    {"name": "Pub A", "location": (40.731, -73.935), "rating": 4.5},
    {"name": "Pub B", "location": (40.732, -73.936), "rating": 4.0},
    {"name": "Pub C", "location": (40.733, -73.937), "rating": 3.5},
    {"name": "Pub D", "location": (40.734, -73.938), "rating": 5.0},
]

# example Distance matrix format: dist_matrix[i][j] is the distance from place i to place j
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25], 
    [15, 35, 0, 30], 
    [20, 25, 30, 0], 
]

# test
path, total_cost = a_star(places, dist_matrix, num_stops)

# Print the resulting path and total cost
if path:
    print("Pub crawl path:")
    for idx in path:
        print(f"{places[idx]['name']} (Rating: {places[idx]['rating']})")
    print(f"Total cost (distance): {total_cost}")
else:
    print("No valid path found.")
"""