from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(collection: Sequence[T]) -> T:
    highest_value: T = collection[0]
    position: int = 0
    while position < len(collection):
        present_item: T = collection[position]
        if not (present_item <= highest_value):
            highest_value = present_item
        position += 1
    return highest_value