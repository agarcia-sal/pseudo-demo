from typing import List


def move_one_ball(array_of_integers: List[int]) -> bool:
    if not array_of_integers:
        return True
    sorted_array = sorted(array_of_integers)
    min_val = min(array_of_integers)
    min_idx = array_of_integers.index(min_val)
    return check_match(0, array_of_integers, sorted_array, min_val, min_idx)


def check_match(
    position: int,
    original_array: List[int],
    sorted_array: List[int],
    minimum_value: int,
    minimum_index: int
) -> bool:
    if not original_array:
        return True

    n = len(original_array)
    rotated_array = original_array[minimum_index:] + original_array[:minimum_index]

    if position >= n:
        return True

    if rotated_array[position] == sorted_array[position]:
        return check_match(position + 1, original_array, sorted_array, minimum_value, minimum_index)
    else:
        return False