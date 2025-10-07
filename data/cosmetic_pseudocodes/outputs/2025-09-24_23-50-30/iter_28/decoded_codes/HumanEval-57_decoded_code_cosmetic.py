from typing import Sequence, Callable, TypeVar

T = TypeVar('T')

def monotonic(data_sequence: Sequence[T]) -> bool:
    def is_sorted(seq: Sequence[T], cmp: Callable[[T, T], bool]) -> bool:
        def check(index: int) -> bool:
            if index >= len(seq) - 1:
                return True
            if not cmp(seq[index], seq[index + 1]):
                return False
            return check(index + 1)
        return check(0)

    def ascending(x: T, y: T) -> bool:
        return x <= y

    def descending(x: T, y: T) -> bool:
        return x >= y

    return is_sorted(data_sequence, ascending) or is_sorted(data_sequence, descending)