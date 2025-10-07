from typing import Sequence

def mean_absolute_deviation(input_sequence: Sequence[float]) -> float:
    def sum_recursive(seq: Sequence[float], index: int, acc: float) -> float:
        if index == len(seq):
            return acc
        else:
            return sum_recursive(seq, index + 1, acc + seq[index])

    def abs_diff_sum(seq: Sequence[float], idx: int, accum: float, ref: float) -> float:
        if idx == len(seq):
            return accum
        else:
            diff = seq[idx] - ref
            mod_diff = diff if diff >= 0 else -diff
            return abs_diff_sum(seq, idx + 1, accum + mod_diff, ref)

    if not input_sequence:
        raise ValueError("input_sequence must not be empty")
    total = sum_recursive(input_sequence, 0, 0.0)
    length = len(input_sequence)
    average = total / length
    deviation_sum = abs_diff_sum(input_sequence, 0, 0.0, average)
    result = deviation_sum / length
    return result