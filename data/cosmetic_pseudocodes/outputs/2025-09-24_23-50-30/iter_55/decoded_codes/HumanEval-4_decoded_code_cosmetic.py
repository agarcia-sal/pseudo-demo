from typing import Sequence


def mean_absolute_deviation(container_of_values: Sequence[float]) -> float:
    length = len(container_of_values)
    if length == 0:
        raise ValueError("container_of_values must not be empty")

    idx: int = 0
    acc_sum: float = 0.0
    while idx < length:
        acc_sum += container_of_values[idx]
        idx += 1
    central_tendency: float = acc_sum / length

    def accumulate_absolute_diff(pos: int, acc_diff: float) -> float:
        if pos >= length:
            return acc_diff
        deviation: float = container_of_values[pos] - central_tendency
        abs_dev: float = deviation if deviation >= 0 else -deviation
        return accumulate_absolute_diff(pos + 1, acc_diff + abs_dev)

    total_deviation: float = accumulate_absolute_diff(0, 0.0)
    result_value: float = total_deviation / length
    return result_value