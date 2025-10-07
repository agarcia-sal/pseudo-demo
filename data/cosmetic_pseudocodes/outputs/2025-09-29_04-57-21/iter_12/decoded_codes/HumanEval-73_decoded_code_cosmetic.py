from typing import List

def smallest_change(array_of_integers: List[int]) -> int:
    difference_count: int = 0
    half_length: int = (len(array_of_integers) // 2) - 1
    current_pos: int = 0
    while current_pos <= half_length:
        if array_of_integers[current_pos] != array_of_integers[len(array_of_integers) - 1 - current_pos]:
            difference_count += 1
        current_pos += 1
    return difference_count