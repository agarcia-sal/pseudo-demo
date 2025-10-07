def sort_array(array):
    if len(array) == 0:
        return []
    sum_first_last = array[0] + array[-1]
    if sum_first_last % 2 == 0:
        result = sorted(array, reverse=True)
    else:
        result = sorted(array)
    return result