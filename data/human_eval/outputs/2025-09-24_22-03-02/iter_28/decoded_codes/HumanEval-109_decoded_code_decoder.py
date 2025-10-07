from typing import List

def move_one_ball(arr: List[int]) -> bool:
    if len(arr) == 0:
        return True
    sorted_array = sorted(arr)
    min_value = min(arr)
    min_index = arr.index(min_value)
    my_arr = arr[min_index:] + arr[:min_index]
    i = 0
    while i < len(arr):
        if my_arr[i] != sorted_array[i]:
            return False
        i += 1
    return True