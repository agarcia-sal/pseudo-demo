def move_one_ball(arr: list) -> bool:
    if len(arr) == 0:
        return True
    sorted_array = sorted(arr)
    min_value = min(arr)
    min_index = arr.index(min_value)
    my_arr = []
    i = min_index
    while i < len(arr):
        my_arr.append(arr[i])
        i += 1
    j = 0
    while j < min_index:
        my_arr.append(arr[j])
        j += 1
    k = 0
    while k < len(arr):
        if my_arr[k] != sorted_array[k]:
            return False
        k += 1
    return True