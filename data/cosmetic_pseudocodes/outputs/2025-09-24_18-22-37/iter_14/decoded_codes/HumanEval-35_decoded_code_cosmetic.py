from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")

def max_element(input_collection: Sequence[T]) -> T:
    highest_value: T = input_collection[0]
    iterator_index: int = 0
    while iterator_index < len(input_collection):
        current_item: T = input_collection[iterator_index]
        if current_item > highest_value:
            highest_value = current_item
        iterator_index += 1
    return highest_value