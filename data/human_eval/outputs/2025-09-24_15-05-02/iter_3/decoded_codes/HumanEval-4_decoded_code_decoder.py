from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    if not numbers:
        return 0.0  # Return 0 for empty list to avoid division by zero
    mean = sum(numbers) / len(numbers)
    total_absolute_difference = sum(abs(x - mean) for x in numbers)
    return total_absolute_difference / len(numbers)