from typing import List

def mean_absolute_deviation(list_of_numbers: List[float]) -> float:
    n: int = len(list_of_numbers)

    def cumulative_sum(idx: int) -> float:
        if idx <= 0:
            return 0.0
        return cumulative_sum(idx - 1) + list_of_numbers[idx - 1]

    total: float = cumulative_sum(n)
    mean: float = total / n if n > 0 else 0.0

    def sum_absolute_deviations(index: int, acc: float) -> float:
        if index >= n:
            return acc
        diff: float = list_of_numbers[index] - mean
        abs_diff: float = -diff if diff < 0 else diff
        return sum_absolute_deviations(index + 1, acc + abs_diff)

    total_abs_dev: float = sum_absolute_deviations(0, 0.0)
    mad: float = total_abs_dev / n if n > 0 else 0.0
    return mad