from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    if not numbers:
        return []

    low: float = numbers[0]
    high: float = numbers[0]
    idx: int = 1
    while idx < len(numbers):
        if numbers[idx] < low:
            low = numbers[idx]
        elif numbers[idx] > high:
            high = numbers[idx]
        idx += 1

    if high == low:
        # Avoid division by zero: if all values are equal, return zeros
        return [0.0 for _ in numbers]

    def normalize(val: float) -> float:
        return (val - low) / (high - low)

    result: List[float] = []
    pos: int = 0
    while pos < len(numbers):
        result.append(normalize(numbers[pos]))
        pos += 1
    return result