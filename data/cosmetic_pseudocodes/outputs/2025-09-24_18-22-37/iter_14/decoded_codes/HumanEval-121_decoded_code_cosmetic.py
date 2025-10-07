from typing import List


def solution(array_of_numbers: List[int]) -> int:
    total_sum: int = 0
    position: int = 0

    while position < len(array_of_numbers):
        element: int = array_of_numbers[position]
        is_position_even: bool = (position % 2) == 0
        is_element_odd: bool = (element % 2) != 0

        if is_position_even and is_element_odd:
            total_sum += element

        position += 1

    return total_sum