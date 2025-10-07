from typing import List

def mean_absolute_deviation(array_input: List[float]) -> float:
    n = len(array_input)
    if n == 0:
        raise ValueError("array_input must not be empty")

    def compute_mean(idx: int, acc: float) -> float:
        if idx == n:
            return acc / n
        return compute_mean(idx + 1, acc + array_input[idx])

    def sum_abs_diff(idx: int, acc_sum: float, center: float) -> float:
        if idx == n:
            return acc_sum
        diff = array_input[idx] - center
        abs_diff = -diff if diff < 0 else diff
        return sum_abs_diff(idx + 1, acc_sum + abs_diff, center)

    average = compute_mean(0, 0.0)
    total_deviation = sum_abs_diff(0, 0.0, average)
    result = total_deviation / n
    return result