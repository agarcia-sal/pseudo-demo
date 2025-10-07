from typing import Sequence, Union

def median(input_sequence: Sequence[Union[int, float]]) -> float:
    ordered_sequence = sorted(input_sequence)
    seq_length = len(ordered_sequence)
    middle = seq_length // 2
    if seq_length % 2 != 0:
        return float(ordered_sequence[middle])
    else:
        return (ordered_sequence[middle - 1] + ordered_sequence[middle]) * 0.5