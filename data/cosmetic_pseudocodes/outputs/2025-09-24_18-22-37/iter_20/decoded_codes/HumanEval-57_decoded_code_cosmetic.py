from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(collection: Sequence[T]) -> bool:
    ascending_order: bool = True
    descending_order: bool = True
    length_val: int = len(collection)
    index: int = 1

    while index < length_val:
        current_val: T = collection[index - 1]
        next_val: T = collection[index]

        if current_val > next_val:
            ascending_order = False
        if current_val < next_val:
            descending_order = False

        if not (ascending_order or descending_order):
            return False

        index += 1

    return True