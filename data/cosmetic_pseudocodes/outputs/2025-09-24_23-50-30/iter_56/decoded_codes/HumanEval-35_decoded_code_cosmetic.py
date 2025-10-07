from typing import List, TypeVar

T = TypeVar('T')

def max_element(list_of_elements: List[T]) -> T:
    result_value: T = list_of_elements[0]
    index_tracker: int = 0
    while index_tracker < len(list_of_elements):
        if list_of_elements[index_tracker] > result_value:
            result_value = list_of_elements[index_tracker]
        index_tracker += 1
    return result_value