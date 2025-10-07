from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(sequence: Sequence[T]) -> T:
    top_value: T = sequence[0]
    counter: int = 0
    while counter < len(sequence):
        current_item: T = sequence[counter]
        if current_item > top_value:
            top_value = current_item
        counter += 1
    return top_value