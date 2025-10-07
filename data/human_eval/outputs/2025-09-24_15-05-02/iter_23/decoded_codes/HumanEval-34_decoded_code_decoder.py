from typing import List, TypeVar

T = TypeVar('T')

def unique(list_input: List[T]) -> List[T]:
    unique_set = set(list_input)  # Remove duplicates
    unique_list = list(unique_set)
    unique_list.sort()  # Sort ascending
    return unique_list