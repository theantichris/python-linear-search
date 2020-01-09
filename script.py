def linear_search(search_list, target_value):
    matches = []

    for i in range(len(search_list)):
        if search_list[i] == target_value:
            matches.append(i)

    if matches:
        return matches

    raise ValueError("{} not in list".format(target_value))

def linear_search_largest(search_list):
    maximum_score_index = None

    for i in range(len(search_list)):
        if maximum_score_index is None or search_list[i] > search_list[maximum_score_index]:
            maximum_score_index = i

    return maximum_score_index


tour_locations = ["New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto"]
target_city = "Knoxville"

try:
    tour_stops = linear_search(tour_locations, target_city)
    print(tour_stops)
except ValueError as error_message:
    print(error_message)
