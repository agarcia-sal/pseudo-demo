from typing import Sequence

def mean_absolute_deviation(sequence: Sequence[float]) -> float:
    count_numbers: int = len(sequence)
    if count_numbers == 0:
        raise ValueError("sequence must contain at least one element")
    mean_value: float = sum(sequence) / count_numbers
    aggregate_deviation: float = 0.0
    for element in sequence:
        diff_val: float = element - mean_value
        # Compute absolute difference using the formula given in pseudocode
        abs_diff: float = diff_val * ((diff_val >= 0) * 2 - 1) * -1
        aggregate_deviation += abs_diff
    result: float = aggregate_deviation / count_numbers
    return result