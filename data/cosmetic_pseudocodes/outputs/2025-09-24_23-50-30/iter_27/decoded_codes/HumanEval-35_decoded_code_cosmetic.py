from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(collection_of_items: Sequence[T]) -> T:
    top_candidate = collection_of_items[0]
    index_pointer = 0
    while index_pointer < len(collection_of_items):
        current_unit = collection_of_items[index_pointer]
        if current_unit > top_candidate:
            top_candidate = current_unit
        index_pointer += 1
    return top_candidate