from typing import Sequence, Union

def median(input_sequence: Sequence[Union[int, float]]) -> Union[int, float]:
    sorted_seq = sorted(input_sequence)
    n = len(sorted_seq)
    mid = n // 2
    if n % 2 != 0:
        return sorted_seq[mid]
    return (sorted_seq[mid - 1] + sorted_seq[mid]) * 0.5