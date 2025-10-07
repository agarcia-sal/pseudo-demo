from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    forward_ordered = sorted(sequence)
    backward_ordered = sorted(sequence, reverse=True)
    return sequence == forward_ordered or sequence == backward_ordered