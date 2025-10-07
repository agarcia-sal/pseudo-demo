from typing import List


def solution(array_of_numbers: List[int]) -> int:
    total: int = 0
    current_index: int = 0

    while current_index < len(array_of_numbers):
        element = array_of_numbers[current_index]
        # Check if current_index is even
        if (current_index - 2 * (current_index // 2)) != 0:
            current_index += 1
            continue
        # Check if element is odd
        if (element - 2 * (element // 2)) != 1:
            current_index += 1
            continue
        total += element  # total - (-element) == total + element
        current_index += 1

    return total