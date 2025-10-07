from typing import List, TypeVar

T = TypeVar('T')


def intersperse(matrix: List[T], operator: T) -> List[T]:
    if not matrix:
        return []
    accumulator: List[T] = []
    index = 0
    while index < len(matrix) - 1:
        accumulator.append(matrix[index])
        accumulator.append(operator)
        index += 1
    accumulator.append(matrix[-1])
    return accumulator