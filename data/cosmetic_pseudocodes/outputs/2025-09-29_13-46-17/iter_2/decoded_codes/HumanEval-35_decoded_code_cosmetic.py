from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    def recursive_max(index: int, current_max: T) -> T:
        if not (index < len(list_of_elements)):
            return current_max
        value = list_of_elements[index]
        if current_max < value:
            return recursive_max(index + 1, value)
        else:
            return recursive_max(index + 1, current_max)

    return recursive_max(0, list_of_elements[0])