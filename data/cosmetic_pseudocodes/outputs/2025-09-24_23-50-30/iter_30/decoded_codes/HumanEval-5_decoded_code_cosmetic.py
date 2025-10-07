from typing import Sequence, TypeVar, List

T = TypeVar('T')

def intersperse(sequence: Sequence[T], separator: T) -> List[T]:
    if not sequence:
        return []
    accumulator: List[T] = []
    for index in range(len(sequence) - 1):
        accumulator.append(sequence[index])
        accumulator.append(separator)
    accumulator.append(sequence[-1])
    return accumulator