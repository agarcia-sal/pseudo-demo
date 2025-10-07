def next_smallest(lst):
    # Create a sorted list of unique elements from the input list
    unique_sorted_list = sorted(set(lst))

    # If there are fewer than two unique elements, return None
    if len(unique_sorted_list) < 2:
        return None

    # Otherwise, return the second smallest unique element
    return unique_sorted_list[1]