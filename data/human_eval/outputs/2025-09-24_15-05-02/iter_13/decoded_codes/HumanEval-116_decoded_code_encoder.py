def sort_array(arr):
    sorted_by_value = sorted(arr)
    sorted_by_ones = sorted(sorted_by_value, key=lambda x: bin(x).count('1'))
    return sorted_by_ones