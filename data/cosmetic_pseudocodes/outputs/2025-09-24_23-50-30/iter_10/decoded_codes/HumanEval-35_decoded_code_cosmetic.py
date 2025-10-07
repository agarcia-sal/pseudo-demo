from typing import TypeVar, Sequence

T = TypeVar('T')

def max_element(collection: Sequence[T]) -> T:
    def find_max(current_index: int, current_max: T) -> T:
        if current_index == len(collection):
            return current_max
        candidate = collection[current_index]
        updated_max = candidate if candidate > current_max else current_max
        return find_max(current_index + 1, updated_max)

    if not collection:
        raise ValueError("max_element() arg is an empty sequence")
    return find_max(1, collection[0])