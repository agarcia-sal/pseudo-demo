from typing import Sequence

def mean_absolute_deviation(series_of_values: Sequence[float]) -> float:
    aggregate_sum: float = 0.0
    count: int = 0
    length: int = len(series_of_values)
    while count < length:
        aggregate_sum += series_of_values[count]
        count += 1
    average: float = aggregate_sum / length if length > 0 else 0.0

    cumulative_diff: float = 0.0
    idx: int = 0
    while idx < length:
        deviation: float = series_of_values[idx] - average
        positive_deviation: float = deviation if deviation >= 0 else -deviation
        cumulative_diff += positive_deviation
        idx += 1

    mad_result: float = cumulative_diff / length if length > 0 else 0.0
    return mad_result