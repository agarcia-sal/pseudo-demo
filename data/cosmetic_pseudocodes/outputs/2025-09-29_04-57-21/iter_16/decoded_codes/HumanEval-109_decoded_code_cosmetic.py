from typing import List


def move_one_ball(array_of_integers: List[int]) -> bool:
    if not array_of_integers:
        return True

    sorted_array = sorted(array_of_integers)
    min_val = min(array_of_integers)
    min_pos = array_of_integers.index(min_val)

    rotated_array = array_of_integers[min_pos:] + array_of_integers[:min_pos]

    for idx in range(len(array_of_integers)):
        if rotated_array[idx] != sorted_array[idx]:
            return False
    return True