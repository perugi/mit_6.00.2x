###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time

# ================================
# Part A: Transporting Space Cows
# ================================


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, "r")

    for line in f:
        line_data = line.split(",")
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    trips = []
    # Copy the cows into a list of lists, sorted by weight.
    remaining_cows = [
        (name, weight)
        for name, weight in sorted(cows.items(), key=lambda i: i[1], reverse=True)
    ]

    while remaining_cows:
        trip = []
        weight = 0
        for cow in remaining_cows.copy():
            # If we can take a cow on-board, do so and remove it from the remaining_cows
            if weight + cow[1] <= limit:
                trip.append(cow[0])
                weight += cow[1]
                remaining_cows.remove(cow)
                # Optimization: if we've reached the limit, no need to go through the rest of the list.
                if weight == limit:
                    break
        trips.append(trip)

        # If we have cows remaining, but could not fit them on a ship, there is no solution.
        if not trip:
            return []

    return trips


# Problem 2
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    trips = []
    # Track the best configuration of trips possible (lowest total number of trips).
    # Set the initial number of best trips to the number of cows + 1 (so that it is
    # guaranteed that at least each cow on a separate ship will be better).
    best_trips = len(cows) + 1

    for partition in get_partitions(cows):
        """partition, generated by get_partitions is a list of trips, each of which is a list of
        cows on-board. The brute force approach is to find a partition where all of the trips
        respect the max weight limit. Because the partitions are returned in order (first partition
        is all cows on a single trip, then all subsets of cows on two trips etc.), we can exit the
        algorithm as soon as an appropriate partition is found."""

        weight_ok_flag = True
        for trip in partition:
            weight = 0
            # Sum the weight of all the cows on the trip and compare to the limit
            for cow in trip:
                weight += cows[cow]
            if weight > limit:
                weight_ok_flag = False
                break

        # We have found a partition where the weight was respected for all trips.
        # Check if it is better than the current best partition
        if weight_ok_flag:
            if len(partition) < best_trips:
                trips = partition
                best_trips = len(partition)

    return trips


# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """

    start = time.time()
    greedy = greedy_cow_transport(cows, 10)
    end = time.time()
    greedy_time = end - start
    greedy_trips = len(greedy)

    start = time.time()
    brute = brute_force_cow_transport(cows, 10)
    end = time.time()
    brute_time = end - start
    brute_trips = len(brute)

    print("-- Algorithm comparison --")
    print(f"Greedy: time = {greedy_time} s, trips = {greedy_trips}")
    print(f"Brute Force: time = {brute_time} s, trips = {brute_trips}")


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit = 20
print(cows)

compare_cow_transport_algorithms()
# print(greedy_cow_transport(cows, limit))
# print(brute_force_cow_transport(cows, limit))
# print( brute_force_cow_transport(
#         {
#             "MooMoo": 50,
#             "Miss Bella": 25,
#             "Milkshake": 40,
#             "Boo": 20,
#             "Horns": 25,
#             "Lotus": 40,
#         },
#         100,
#     )
# )
# print(brute_force_cow_transport({"Daisy": 50, "Buttercup": 72, "Betsy": 65}, 75))