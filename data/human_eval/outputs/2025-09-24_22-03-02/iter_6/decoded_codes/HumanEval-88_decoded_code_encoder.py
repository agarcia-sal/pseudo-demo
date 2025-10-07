def sort_array(array):
    if len(array) == 0:
        return []
    sum_first_last = array[0] + array[-1]
    should_sort_descending = (sum_first_last % 2 == 0)
    return sorted(array, reverse=should_sort_descending)