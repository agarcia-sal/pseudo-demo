from typing import TypeVar, Sequence

T = TypeVar("T")


def max_element(list_of_elements: Sequence[T]) -> T:
    greatest_so_far: T = list_of_elements[0]
    index_counter: int = 0
    length = len(list_of_elements)
    while index_counter < length:
        current_candidate = list_of_elements[index_counter]
        if not (current_candidate <= greatest_so_far):
            greatest_so_far = current_candidate
        index_counter += 1
    return greatest_so_far