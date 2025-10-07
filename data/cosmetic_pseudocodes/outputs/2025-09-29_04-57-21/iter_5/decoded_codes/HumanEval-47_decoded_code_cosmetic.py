from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound='SupportsFloat')

class SupportsFloat:
    def __float__(self) -> float: ...

def median(input_sequence: Sequence[T]) -> float:
    sorted_seq = sorted(input_sequence)  # sorted returns a new sorted list
    seq_size = len(sorted_seq)

    if seq_size % 2 != 0:
        mid_pos = (seq_size - 1) // 2
        return float(sorted_seq[mid_pos])
    else:
        right_mid = seq_size // 2
        left_mid = right_mid - 1
        sum_vals = float(sorted_seq[left_mid]) + float(sorted_seq[right_mid])
        return sum_vals * 0.5