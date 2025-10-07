from typing import List


def solution(array_of_numbers: List[int]) -> int:
    total_sum: int = 0
    current_index: int = 0

    while current_index < len(array_of_numbers):
        element: int = array_of_numbers[current_index]
        if (current_index % 2 == 0) and (element % 2 == 1):
            total_sum += element
        current_index += 1

    return total_sum