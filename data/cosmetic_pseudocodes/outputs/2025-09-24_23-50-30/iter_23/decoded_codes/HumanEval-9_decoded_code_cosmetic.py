from typing import List, Optional, TypeVar, Sequence

T = TypeVar('T')

def rolling_max(sequence: List[T]) -> List[T]:
    result_sequence: List[T] = []
    accumulator: Optional[T] = None

    while sequence:
        current = sequence.pop(0)
        if accumulator is None:
            accumulator = current
        else:
            accumulator = accumulator if accumulator > current else current
        result_sequence.append(accumulator)

    return result_sequence