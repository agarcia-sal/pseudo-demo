from typing import Sequence, TypeVar

T = TypeVar('T')


def max_element(collection_of_items: Sequence[T]) -> T:
    def step(index: int, current_max: T) -> T:
        if index == len(collection_of_items):
            return current_max
        candidate = collection_of_items[index]
        next_max = candidate if candidate > current_max else current_max
        return step(index + 1, next_max)

    if not collection_of_items:
        raise ValueError("max_element() arg is an empty sequence")
    return step(0, collection_of_items[0])