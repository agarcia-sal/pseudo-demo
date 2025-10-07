from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(container: Sequence[T]) -> T:
    def rec_find_max(index: int, current_max: T) -> T:
        if index == len(container):
            return current_max
        candidate = container[index]
        next_max = current_max if candidate <= current_max else candidate
        return rec_find_max(index + 1, next_max)
    return rec_find_max(1, container[0])