def sort_array(array):
    if len(array) == 0:
        return []
    else:
        sum_first_last = array[0] + array[-1]
        is_sum_even = (sum_first_last % 2) == 0
        sorted_array = sorted(array, reverse=is_sum_even)
        return sorted_array