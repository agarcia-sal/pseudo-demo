def move_one_ball(arr):
    # If the array is empty, return True
    if len(arr) == 0:
        return True

    # Sorted version of arr in non-decreasing order
    sorted_array = sorted(arr)

    # Find minimum value and its index in original array
    min_value = min(arr)
    min_index = arr.index(min_value)

    # Rotate the array starting from min_index
    rotated_arr = arr[min_index:] + arr[:min_index]

    # Check if rotated array matches the sorted array
    return rotated_arr == sorted_array