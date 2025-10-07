from typing import Sequence


def mean_absolute_deviation(seq: Sequence[float]) -> float:
    def abs_diff_sum(accum: float, idx: int) -> float:
        if idx == len(seq):
            return accum
        delta = seq[idx] - avg
        updated_accum = accum + (-delta if delta < 0 else delta)
        return abs_diff_sum(updated_accum, idx + 1)

    avg: float = sum(seq) / len(seq)
    result: float = abs_diff_sum(0.0, 0) / len(seq)
    return result