from typing import Sequence, Union

def median(sequence: Sequence[Union[int, float]]) -> float:
    sorted_seq = sorted(sequence)
    n = len(sorted_seq)
    if n == 0:
        raise ValueError("median() arg is an empty sequence")
    if n % 2 == 1:
        return float(sorted_seq[n // 2])
    else:
        half = n // 2
        return (sorted_seq[half - 1] + sorted_seq[half]) / 2.0