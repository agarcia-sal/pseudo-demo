from typing import List

def move_one_ball(arr: List[int]) -> bool:
    if len(arr) == 0:
        return True
    sorted_array = sorted(arr)
    min_value = min(arr)
    min_index = arr.index(min_value)
    my_arr = arr[min_index:] + arr[:min_index]
    for index in range(len(arr)):
        if my_arr[index] != sorted_array[index]:
            return False
    return True