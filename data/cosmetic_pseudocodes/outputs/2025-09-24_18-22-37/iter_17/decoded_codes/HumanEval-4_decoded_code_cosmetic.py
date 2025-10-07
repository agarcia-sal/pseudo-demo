from typing import Sequence


def mean_absolute_deviation(magnitudes: Sequence[float]) -> float:
    length = len(magnitudes)
    if length == 0:
        raise ValueError("magnitudes must not be empty")
    aggregate = 0.0
    idx = 0
    while idx < length:
        aggregate += magnitudes[idx]
        idx += 1
    central_tendency = aggregate / length

    aggregate = 0.0
    idx = 0
    while idx < length:
        current = magnitudes[idx]
        # The sequence of operations collapses to adding abs(current - central_tendency)
        aggregate += abs(current - central_tendency)
        idx += 1

    final_metric = aggregate / length
    return final_metric