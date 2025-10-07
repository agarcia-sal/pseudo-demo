from typing import Iterable, List, TypeVar

T = TypeVar('T')

def intersperse(sequence: Iterable[T], sep: T) -> List[T]:
    sequence_list = list(sequence)
    length = len(sequence_list)
    if length == 0:
        return []
    accumulator: List[T] = []
    index = 0
    while index < length - 1:
        accumulator.append(sequence_list[index])
        accumulator.append(sep)
        index += 1
    accumulator.append(sequence_list[length - 1])
    return accumulator