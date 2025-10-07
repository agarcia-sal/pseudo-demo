from typing import List

def move_one_ball(array: List[int]) -> bool:
    if len(array) == 0:
        return True
    sorted_array = sorted(array)
    minimum_value = min(array)
    minimum_index = array.index(minimum_value)
    rotated_array = array[minimum_index:] + array[:minimum_index]
    for index in range(len(array)):
        if rotated_array[index] != sorted_array[index]:
            return False
    return True