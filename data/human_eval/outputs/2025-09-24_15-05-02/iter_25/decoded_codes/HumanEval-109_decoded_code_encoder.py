from typing import List

def move_one_ball(array: List[int]) -> bool:
    if not array:
        return True

    sorted_array = sorted(array)
    min_value = min(array)
    min_index = array.index(min_value)

    rotated_array = array[min_index:] + array[:min_index]

    return all(rotated_array[i] == sorted_array[i] for i in range(len(array)))