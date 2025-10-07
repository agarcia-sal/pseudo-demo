from typing import List


def smallest_change(array_of_integers: List[int]) -> int:
    discrepancy_count: int = 0
    max_index: int = len(array_of_integers)
    midpoint: float = (max_index / 2) - 1
    current_position: int = 0

    while current_position <= midpoint:
        front_value: int = array_of_integers[current_position]
        rear_value: int = array_of_integers[max_index - current_position - 1]
        if front_value != rear_value:
            discrepancy_count += 1
        current_position += 1

    return discrepancy_count