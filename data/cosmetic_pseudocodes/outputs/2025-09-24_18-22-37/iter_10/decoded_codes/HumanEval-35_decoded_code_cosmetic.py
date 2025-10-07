from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(collection: Sequence[T]) -> T:
    frontier: int = 0
    highest: T = collection[frontier]

    while frontier < len(collection):
        current: T = collection[frontier]

        if not (current <= highest):
            highest = current

        frontier += 1

    return highest