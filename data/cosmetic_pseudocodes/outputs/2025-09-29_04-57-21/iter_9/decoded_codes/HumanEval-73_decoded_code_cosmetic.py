from typing import List


def smallest_change(array_of_integers: List[int]) -> int:
    discrepancy_count: int = 0
    halfway_point: int = len(array_of_integers) // 2
    current_position: int = 0

    while current_position < halfway_point:
        left_value: int = array_of_integers[current_position]
        right_value: int = array_of_integers[len(array_of_integers) - current_position - 1]

        if left_value != right_value:
            discrepancy_count += 1

        current_position += 1

    return discrepancy_count