from typing import List, TypeVar

T = TypeVar('T')

def intersperse(sequence_values: List[T], gap_element: T) -> List[T]:
    if len(sequence_values) == 0:
        return []

    accumulator: List[T] = []
    idx: int = 0
    limit: int = len(sequence_values) - 1

    while idx < limit:
        accumulator.extend([sequence_values[idx], gap_element])
        idx += 1

    accumulator.append(sequence_values[limit])
    return accumulator