from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(collection: Sequence[T]) -> T:
    def find_maximum(index: int, current_max: T) -> T:
        if index == len(collection):
            return current_max
        new_max = current_max
        if collection[index] > current_max:
            new_max = collection[index]
        return find_maximum(index + 1, new_max)
    return find_maximum(0, collection[0])