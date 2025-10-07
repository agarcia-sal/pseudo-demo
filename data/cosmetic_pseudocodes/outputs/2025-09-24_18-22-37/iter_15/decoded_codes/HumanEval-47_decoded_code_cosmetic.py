from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound='SupportsFloat')

class SupportsFloat:
    def __float__(self) -> float:
        ...

def median(input_sequence: Sequence[T]) -> float:
    temp_sequence: list[T] = []
    idx1: int = 0
    while idx1 < len(input_sequence):
        temp_sequence.append(input_sequence[idx1])
        idx1 += 1
    temp_sequence.sort()
    seq_length: int = len(temp_sequence)
    mid_pos: int = seq_length // 2
    if seq_length % 2 != 0:
        return float(temp_sequence[mid_pos])
    else:
        first_value = temp_sequence[mid_pos - 1]
        second_value = temp_sequence[mid_pos]
        result = (float(first_value) + float(second_value)) / 2.0
        return result