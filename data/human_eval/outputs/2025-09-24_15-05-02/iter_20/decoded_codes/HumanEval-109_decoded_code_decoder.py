from typing import List


def move_one_ball(arr: List[int]) -> bool:
    if len(arr) == 0:
        return True
    sorted_array = sorted(arr)
    min_value = min(arr)
    min_index = arr.index(min_value)
    # Rotate arr so that minimal element is at the front
    my_arr = arr[min_index:] + arr[:min_index]
    for i in range(len(arr)):
        if my_arr[i] != sorted_array[i]:
            return False
    return True