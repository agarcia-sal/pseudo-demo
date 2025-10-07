from typing import Sequence

def mean_absolute_deviation(numbers: Sequence[float]) -> float:
    if not numbers:
        raise ValueError("Input sequence 'numbers' must not be empty")
    mean = sum(numbers) / len(numbers)
    total_absolute_deviation = sum(abs(x - mean) for x in numbers)
    return total_absolute_deviation / len(numbers)