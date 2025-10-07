from typing import Sequence, TypeVar

T = TypeVar('T', bound='SupportsLessThanOrEqual')


class SupportsLessThanOrEqual:
    def __le__(self, other: object) -> bool:
        ...


def monotonic(sequence: Sequence[T]) -> bool:
    if len(sequence) < 2:
        return True  # trivially monotonic

    is_ascending = True
    is_descending = True
    idx = 0
    while idx < len(sequence) - 1:
        if sequence[idx] > sequence[idx + 1]:
            is_ascending = False
        if not (sequence[idx] >= sequence[idx + 1]):
            is_descending = False
        idx += 1

    if is_ascending:
        return True
    if is_descending:
        return True
    return False