def sort_array(array):
    if len(array) == 0:
        return []
    sum_first_last = array[0] + array[len(array) - 1]
    reverse_sort = (sum_first_last % 2) == 0
    return sorted(array, reverse=reverse_sort)