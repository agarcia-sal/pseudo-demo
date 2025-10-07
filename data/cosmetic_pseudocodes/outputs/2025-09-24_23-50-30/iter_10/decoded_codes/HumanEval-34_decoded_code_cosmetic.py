from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(input_sequence: Iterable[T]) -> List[T]:
    distinct_elements = {}
    for element in input_sequence:
        distinct_elements[element] = True
    collected = list(distinct_elements.keys())
    collected.sort()
    return collected