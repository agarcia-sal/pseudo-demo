from typing import List, TypeVar

T = TypeVar('T')
U = TypeVar('U')

def intersperse(numbers: List[T], delimeter: U) -> List:
    if not numbers:
        return []

    result: List = []
    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)
    result.append(numbers[-1])
    return result