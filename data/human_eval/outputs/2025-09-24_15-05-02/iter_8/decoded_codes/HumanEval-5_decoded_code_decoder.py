from typing import List, TypeVar

T = TypeVar('T')

def intersperse(numbers: List[T], delimiter: T) -> List[T]:
    if not numbers:
        return []
    result: List[T] = []
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimiter)
    result.append(numbers[-1])
    return result