def sort_array(arr):
    sorted_arr = sorted(arr)
    sorted_arr = sorted(sorted_arr, key=lambda x: bin(x).count('1'))
    return sorted_arr