from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    if not list_of_numbers:
        return 0.0  # Return 0.0 for empty input to avoid division by zero
    mean_value: float = sum(list_of_numbers) / len(list_of_numbers)
    total_absolute_deviation: float = sum(abs(number - mean_value) for number in list_of_numbers)
    mean_absolute_deviation: float = total_absolute_deviation / len(list_of_numbers)
    return mean_absolute_deviation