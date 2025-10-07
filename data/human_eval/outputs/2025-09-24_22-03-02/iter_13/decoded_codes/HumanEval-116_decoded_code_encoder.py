def sort_array(arr):
    return sorted(arr, key=lambda x: bin(x)[2:].count('1'))