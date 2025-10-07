from typing import List

def move_one_ball(list_of_integers: List[int]) -> bool:
    if not list_of_integers:
        return True

    sorted_array = sorted(list_of_integers)
    minimum_value = min(list_of_integers)
    minimum_index = list_of_integers.index(minimum_value)

    rotated_array = list_of_integers[minimum_index:] + list_of_integers[:minimum_index]

    return rotated_array == sorted_array