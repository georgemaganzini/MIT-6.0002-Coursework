###########################
# 6.0002 Problem Set 1a: Space Cows
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import copy

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
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
    cows = {}
    cows_file = open(filename, 'r')
    for line in cows_file:
        line = line.rstrip()
        key_value = line.split(',')
        cows[key_value[0]] = key_value[1]
    cows_file.close()

    return cows

cows = load_cows('ps1_cow_data.txt')

# Problem 2
def greedy_cow_transport(cows,limit=10):
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
    # make a list of tuples from input dict sorted by weight descending
    cows_to_be_xported = [(k, int(v)) for k, v in sorted(cows.items(), key=lambda x: x[1], reverse=True)]

    # instantiate results list (of lists)
    results = []

    # while loop until there are no more cows below overall weight limit
    while any(v < limit for (k, v) in cows_to_be_xported):

        current_limit = limit # current trip weight limit

        current_manifest = [] # current trip manifest

        cows_to_remove = [] # indices of cows that have already been transported

        # add cows to current trip if they fit, in order of heaviest to lightest
        for i in range(len(cows_to_be_xported)):
            (cow, name, weight) = (cows_to_be_xported[i], cows_to_be_xported[i][0], cows_to_be_xported[i][1]) # semantic variable name options

            if weight < current_limit:
                current_limit -= weight # adjust current trip limit for added cow
                current_manifest.append(name) # add cow to flight manifest
                cows_to_remove.append(i) # store index to remove after iteration is over

        results.append(current_manifest)

        for e in sorted(cows_to_remove, reverse=True): #remove largest indices first to not shuffle list
            cows_to_be_xported.pop(e)

    return results


greedy_cow_transport(cows,limit=10)

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
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
    # TODO: Your code here
    pass

# Problem 4
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
    # TODO: Your code here
    pass
