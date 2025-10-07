from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(seq: Sequence[T]) -> bool:
    temp_seq = sorted(seq)
    return seq == temp_seq or seq == temp_seq[::-1]