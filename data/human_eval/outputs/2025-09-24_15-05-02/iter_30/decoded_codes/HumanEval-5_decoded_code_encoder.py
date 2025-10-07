from typing import List, TypeVar

T = TypeVar('T')

def intersperse(numbers: List[T], delimeter: T) -> List[T]:
    if not numbers:
        return []
    result: List[T] = []
    for number in numbers[:-1]:
        result.append(number)
        result.append(delimeter)
    result.append(numbers[-1])
    return result