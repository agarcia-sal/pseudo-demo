from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=float)

def get_positive(sequence_container: Sequence[T]) -> List[T]:
    accumulator: List[T] = []
    index: int = 0
    while index < len(sequence_container):
        if sequence_container[index] > 0:
            accumulator.append(sequence_container[index])
        index += 1
    return accumulator