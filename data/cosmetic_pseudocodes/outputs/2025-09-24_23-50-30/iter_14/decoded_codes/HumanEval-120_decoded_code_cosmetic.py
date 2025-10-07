from typing import List, TypeVar

T = TypeVar('T')

def maximum(numbers: List[T], count: int) -> List[T]:
    if count == 0:
        return []
    ordered = sorted(numbers)
    size = len(ordered)
    # Collect the last 'count' elements from the sorted list
    result: List[T] = [ordered[index] for index in range(size - count, size)]
    return result