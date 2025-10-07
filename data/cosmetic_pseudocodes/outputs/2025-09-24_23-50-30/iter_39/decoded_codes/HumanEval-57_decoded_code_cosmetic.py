from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    order_forward = sorted(sequence)
    order_backward = sorted(sequence, reverse=True)
    if sequence == order_forward:
        return True
    if sequence == order_backward:
        return True
    return False