from typing import List

def move_one_ball(array_of_integers: List[int]) -> bool:
    if len(array_of_integers) == 0:
        return True

    sorted_array = sorted(array_of_integers)
    minimum_value = min(array_of_integers)
    minimum_index = array_of_integers.index(minimum_value)
    rotated_array = array_of_integers[minimum_index:] + array_of_integers[:minimum_index]

    for index in range(len(array_of_integers)):
        if rotated_array[index] != sorted_array[index]:
            return False
    return True