from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(seq: Sequence[T]) -> T:
    def find_max(idx: int, current_max: T) -> T:
        if idx >= len(seq):
            return current_max
        if not (seq[idx] <= current_max):
            return find_max(idx + 1, seq[idx])
        else:
            return find_max(idx + 1, current_max)
    return find_max(0, seq[0])