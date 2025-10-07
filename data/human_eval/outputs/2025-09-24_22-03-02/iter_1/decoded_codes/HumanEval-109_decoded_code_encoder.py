def is_sorted_rotated(arr):
    if not arr:
        return True
    sorted_arr = sorted(arr)
    min_i = arr.index(min(arr))
    rotated = arr[min_i:] + arr[:min_i]
    return rotated == sorted_arr