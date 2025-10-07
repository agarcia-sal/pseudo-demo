def sort_array(array):
    if len(array) == 0:
        return []
    sum_first_last = array[0] + array[len(array) - 1]
    if sum_first_last % 2 == 0:
        sorted_array = sorted(array, reverse=True)
    else:
        sorted_array = sorted(array)
    return sorted_array