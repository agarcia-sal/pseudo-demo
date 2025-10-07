from typing import List, TypeVar

T = TypeVar("T")

def unique(list_of_elements: List[T]) -> List[T]:
    temporary_set: set[T] = set()
    for entry in list_of_elements:
        temporary_set.add(entry)
    accumulator: List[T] = []
    for item in temporary_set:
        accumulator.append(item)
    accumulator.sort()
    return accumulator