from typing import List

def get_positive(numbers: List[int]) -> List[int]:
    positives: List[int] = []
    index: int = 0
    while index < len(numbers):
        if 0 < numbers[index]:
            positives.append(numbers[index])
        index += 1
    return positives