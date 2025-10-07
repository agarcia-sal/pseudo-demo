def sort_array(array):
    if len(array) == 0:
        return []
    sum_of_ends = array[0] + array[-1]
    is_even = (sum_of_ends % 2) == 0
    return sorted(array, reverse=is_even)