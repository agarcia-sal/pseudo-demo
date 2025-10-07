from typing import Sequence


def mean_absolute_deviation(array_of_values: Sequence[float]) -> float:
    total = 0.0
    n = len(array_of_values)
    if n == 0:
        return 0.0  # Avoid division by zero for empty input
    for i in range(n):
        total += array_of_values[i]
    central_point = total / n

    def compute_deviation(i: int) -> float:
        if i == n:
            return 0.0
        gap = array_of_values[i] - central_point
        abs_gap = -gap if gap < 0 else gap
        return abs_gap + compute_deviation(i + 1)

    deviation_sum = compute_deviation(0)
    return deviation_sum / n