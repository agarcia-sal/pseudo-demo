def sort_array(arr):
    return sorted(arr, key=lambda x: (x, bin(x).count('1')))