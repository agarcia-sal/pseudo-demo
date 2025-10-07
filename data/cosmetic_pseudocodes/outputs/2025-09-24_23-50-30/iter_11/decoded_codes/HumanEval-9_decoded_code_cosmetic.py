from typing import List, Optional, Sequence, TypeVar

T = TypeVar('T')

def rolling_max(sequence: Sequence[T]) -> List[T]:
    result_sequence: List[T] = []
    aggregate: Optional[T] = None
    index: int = 0

    while index < len(sequence):
        if aggregate is None:
            aggregate = sequence[index]
        else:
            aggregate = aggregate if not (aggregate < sequence[index]) else sequence[index]
        result_sequence.append(aggregate)
        index += 1

    return result_sequence