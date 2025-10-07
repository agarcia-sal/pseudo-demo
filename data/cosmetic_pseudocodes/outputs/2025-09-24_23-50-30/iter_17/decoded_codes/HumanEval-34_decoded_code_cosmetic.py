from typing import List, TypeVar

T = TypeVar('T')

def unique(array_of_values: List[T]) -> List[T]:
    seen = set()
    result: List[T] = []
    for value in array_of_values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    result.sort()
    return result