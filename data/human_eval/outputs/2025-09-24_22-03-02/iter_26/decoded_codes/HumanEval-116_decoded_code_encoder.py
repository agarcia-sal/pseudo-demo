def sort_array(arr):
    sorted_arr = sorted(arr)
    sorted_by_ones = sorted(sorted_arr, key=lambda x: bin(x)[2:].count('1'))
    return sorted_by_ones