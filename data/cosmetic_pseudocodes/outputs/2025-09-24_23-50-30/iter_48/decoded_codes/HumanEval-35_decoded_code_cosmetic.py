from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(collection: Sequence[T]) -> T:
    highest_value: T = collection[0]
    index_counter: int = 0
    while index_counter < len(collection):
        if not (collection[index_counter] <= highest_value):
            highest_value = collection[index_counter]
        index_counter += 1
    return highest_value