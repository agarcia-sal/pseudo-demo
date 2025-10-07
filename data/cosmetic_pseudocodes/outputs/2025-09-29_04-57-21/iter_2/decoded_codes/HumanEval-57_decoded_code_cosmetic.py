from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(sequence: Sequence[T]) -> bool:
    return not (sequence > sorted(sequence)) and not (sequence < sorted(sequence, reverse=True))