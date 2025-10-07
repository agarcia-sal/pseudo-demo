from typing import List


def solution(array_of_numbers: List[int]) -> int:
    total: int = 0
    for position in range(len(array_of_numbers)):
        # Condition: NOT (position is odd OR array_of_numbers[position] is odd)
        # Which means: position is even AND array_of_numbers[position] is even
        if not (position % 2 != 0 or array_of_numbers[position] % 2 != 1):
            total += array_of_numbers[position]
    return total