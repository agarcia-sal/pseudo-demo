def sort_array(array):
    if len(array) == 0:
        return []
    sum_of_first_and_last = array[0] + array[-1]
    is_sum_even = (sum_of_first_and_last % 2) == 0
    return sorted(array, reverse=is_sum_even)