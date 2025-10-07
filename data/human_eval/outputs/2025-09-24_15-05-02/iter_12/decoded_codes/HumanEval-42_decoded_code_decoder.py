from typing import List, TypeVar

T = TypeVar('T', int, float)

def incr_list(list_of_elements: List[T]) -> List[T]:
    return [element + 1 for element in list_of_elements]