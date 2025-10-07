from typing import Sequence, TypeVar

T = TypeVar('T', covariant=True)

def monotonic(sequence: Sequence[T]) -> bool:
    sorted_version_left = sorted(sequence)
    sorted_version_right = sorted(sequence, reverse=True)
    if list(sequence) == sorted_version_left or list(sequence) == sorted_version_right:
        return True
    return False