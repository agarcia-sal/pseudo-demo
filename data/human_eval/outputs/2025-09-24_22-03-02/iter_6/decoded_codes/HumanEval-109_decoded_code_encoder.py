def move_one_ball(arr) -> bool:
    if len(arr) == 0:
        return True

    sorted_array = sorted(arr)
    min_value = min(arr)
    min_index = arr.index(min_value)
    rotated_array = arr[min_index:] + arr[:min_index]

    for i in range(len(arr)):
        if rotated_array[i] != sorted_array[i]:
            return False

    return True