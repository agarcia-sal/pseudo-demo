from typing import List


def move_one_ball(array_of_integers: List[int]) -> bool:
    if not array_of_integers:
        return True
    sorted_array = sorted(array_of_integers)
    minimum_value = min(array_of_integers)
    minimum_index = array_of_integers.index(minimum_value)
    rotated_array = array_of_integers[minimum_index:] + array_of_integers[:minimum_index]
    return all(rotated_array[i] == sorted_array[i] for i in range(len(array_of_integers)))