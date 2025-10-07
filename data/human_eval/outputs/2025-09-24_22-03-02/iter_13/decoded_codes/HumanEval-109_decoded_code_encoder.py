def move_one_ball(arr) -> bool:
    if len(arr) == 0:
        return True
    sorted_array = sorted(arr)
    min_value = min(arr)
    min_index = arr.index(min_value)
    my_arr = arr[min_index:] + arr[:min_index]
    return all(my_arr[i] == sorted_array[i] for i in range(len(arr)))