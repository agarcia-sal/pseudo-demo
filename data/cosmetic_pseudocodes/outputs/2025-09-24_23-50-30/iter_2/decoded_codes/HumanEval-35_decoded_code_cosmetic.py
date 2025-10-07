from typing import Sequence, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: Sequence[T]) -> T:
    def helper(index: int, current_max: T) -> T:
        if index == len(list_of_elements):
            return current_max
        elif current_max >= list_of_elements[index]:
            return helper(index + 1, current_max)
        else:
            return helper(index + 1, list_of_elements[index])
    return helper(1, list_of_elements[0])