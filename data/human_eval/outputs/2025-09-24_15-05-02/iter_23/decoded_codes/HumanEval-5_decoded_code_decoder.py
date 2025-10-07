from typing import List, TypeVar, Sequence

T = TypeVar("T")

def intersperse(numbers: Sequence[T], delimeter: T) -> List[T]:
    if not numbers:
        return []
    result: List[T] = []
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)
    result.append(numbers[-1])
    return result