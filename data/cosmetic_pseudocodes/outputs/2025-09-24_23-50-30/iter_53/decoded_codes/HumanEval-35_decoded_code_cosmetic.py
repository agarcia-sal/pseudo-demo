from typing import Sequence, TypeVar

T = TypeVar('T')


def max_element(container: Sequence[T]) -> T:
    def finder(seq: Sequence[T], idx: int, curr_max: T) -> T:
        if idx >= len(seq):
            return curr_max
        if not seq[idx] <= curr_max:
            return finder(seq, idx + 1, seq[idx])
        return finder(seq, idx + 1, curr_max)
    return finder(container, 0, container[0])