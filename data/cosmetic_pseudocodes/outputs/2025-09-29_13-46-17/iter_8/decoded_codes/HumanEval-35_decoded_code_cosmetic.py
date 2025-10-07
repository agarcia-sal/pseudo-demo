from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    def recursive_find(xs: List[T], current_max: T) -> T:
        if not xs:
            return current_max
        head, *tail = xs
        return recursive_find(tail, current_max if not (head > current_max) else head)

    return recursive_find(list_of_elements, list_of_elements[0])