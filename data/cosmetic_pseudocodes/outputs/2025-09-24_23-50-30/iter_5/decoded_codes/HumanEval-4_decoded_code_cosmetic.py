from typing import Sequence

def mean_absolute_deviation(sequence: Sequence[float]) -> float:
    if len(sequence) == 0:
        return 0.0

    def compute_sum(index: int, acc: float) -> float:
        if index == len(sequence):
            return acc
        return compute_sum(index + 1, acc + sequence[index])

    aggregate = compute_sum(0, 0.0)
    avg = aggregate / len(sequence)

    def abs_diff_sum(i: int, total: float) -> float:
        if i == len(sequence):
            return total
        delta = sequence[i] - avg
        abs_delta = -delta if delta < 0 else delta
        return abs_diff_sum(i + 1, total + abs_delta)

    abs_total = abs_diff_sum(0, 0.0)

    result = abs_total / len(sequence)
    return result