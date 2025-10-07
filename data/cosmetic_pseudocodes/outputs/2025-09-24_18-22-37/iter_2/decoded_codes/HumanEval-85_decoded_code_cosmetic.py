from typing import List

def add(numbers: List[int]) -> int:
    total: int = 0
    index: int = 1
    while index < len(numbers):
        if numbers[index] % 2 == 0:
            total += numbers[index]
        index += 2
    return total