from typing import List, TypeVar

T = TypeVar('T')

def maximum(values: List[T], count: int) -> List[T]:
    if count == 0:
        return []
    sorted_values = sorted(values)
    return sorted_values[-count:]