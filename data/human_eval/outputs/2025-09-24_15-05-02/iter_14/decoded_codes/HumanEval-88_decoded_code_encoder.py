def sort_array(array):
    if len(array) == 0:
        return []
    reverse_order = ((array[0] + array[len(array) - 1]) % 2) == 0
    return sorted(array, reverse=reverse_order)