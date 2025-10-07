from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    def find_max_rec(current_max: T, remaining_elements: List[T]) -> T:
        if not remaining_elements:
            return current_max
        head_element = remaining_elements[0]
        tail_elements = remaining_elements[1:]
        if not (head_element <= current_max):
            return find_max_rec(head_element, tail_elements)
        else:
            return find_max_rec(current_max, tail_elements)

    return find_max_rec(list_of_elements[0], list_of_elements)