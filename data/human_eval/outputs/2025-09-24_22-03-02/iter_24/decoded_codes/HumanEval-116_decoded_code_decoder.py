def sort_array(arr):
    sorted_arr = sorted(arr)
    sorted_arr = sorted(sorted_arr, key=lambda x: sum(1 for c in bin(x)[2:] if c == '1'))
    return sorted_arr