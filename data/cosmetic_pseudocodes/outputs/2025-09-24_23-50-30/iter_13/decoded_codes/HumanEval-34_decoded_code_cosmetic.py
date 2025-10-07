from typing import List, TypeVar

T = TypeVar('T')

def unique(list_input: List[T]) -> List[T]:
    set_output = set()
    for element in list_input:
        set_output.add(element)
    array_results = list(set_output)
    return sorted(array_results)