def sort_array(array):
    if len(array) == 0:
        return []
    else:
        sum_first_last = array[0] + array[-1]
        result = array.copy()
        result.sort(reverse=(sum_first_last % 2 == 0))
        return result