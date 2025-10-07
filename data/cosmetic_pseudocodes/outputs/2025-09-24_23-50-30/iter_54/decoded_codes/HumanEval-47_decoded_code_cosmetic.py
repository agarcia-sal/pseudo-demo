from typing import Sequence, Union

def median(sequence: Sequence[Union[int, float]]) -> float:
    ordered_sequence = sorted(sequence)
    half = len(ordered_sequence) // 2
    if len(ordered_sequence) % 2 != 0:
        return float(ordered_sequence[half])
    else:
        return (ordered_sequence[half - 1] + ordered_sequence[half]) * 0.5