def sort_array(array):
    if len(array) == 0:
        return []

    sum_of_first_and_last = array[0] + array[-1]

    if sum_of_first_and_last % 2 == 0:
        result = sorted(array, reverse=True)
    else:
        result = sorted(array)

    return result