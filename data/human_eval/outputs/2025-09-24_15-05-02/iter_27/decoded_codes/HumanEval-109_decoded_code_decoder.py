from typing import List

def move_one_ball(arr: List[int]) -> bool:
    if len(arr) == 0:
        return True
    sorted_array: List[int] = sorted(arr)
    min_value: int = min(arr)
    min_index: int = arr.index(min_value)
    rotated_arr: List[int] = arr[min_index:] + arr[:min_index]
    return all(rotated_arr[i] == sorted_array[i] for i in range(len(arr)))