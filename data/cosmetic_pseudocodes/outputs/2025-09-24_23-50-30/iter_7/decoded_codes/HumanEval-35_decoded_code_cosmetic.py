from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(collection: Sequence[T]) -> T:
    def find_max(index: int, current_max: T) -> T:
        if index >= len(collection):
            return current_max
        return find_max(index + 1, collection[index] if collection[index] > current_max else current_max)
    return find_max(0, collection[0])