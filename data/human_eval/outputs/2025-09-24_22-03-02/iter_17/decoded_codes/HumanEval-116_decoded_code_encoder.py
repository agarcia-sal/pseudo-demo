def sort_array(arr):
    sorted_arr = sorted(arr)
    result = sorted(sorted_arr, key=lambda x: bin(x)[2:].count('1'))
    return result