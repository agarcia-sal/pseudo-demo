from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val: float = numbers[0]
    max_val: float = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    range_val: float = max_val - min_val
    if range_val == 0:
        return [0.0 for _ in numbers]  # All numbers are equal

    def normalize(index: int) -> List[float]:
        if index == len(numbers):
            return []
        scaled: float = (numbers[index] - min_val) / range_val
        return [scaled] + normalize(index + 1)

    return normalize(1)