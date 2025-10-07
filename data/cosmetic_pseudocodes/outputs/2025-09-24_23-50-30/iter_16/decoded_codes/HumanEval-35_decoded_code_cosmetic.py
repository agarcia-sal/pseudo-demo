from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(collection: Sequence[T]) -> T:
    candidate: T = collection[0]

    def find_max(i: int, current_max: T) -> T:
        if i == len(collection):
            return current_max
        elif current_max < collection[i]:
            return find_max(i + 1, collection[i])
        else:
            return find_max(i + 1, current_max)

    return find_max(1, candidate)