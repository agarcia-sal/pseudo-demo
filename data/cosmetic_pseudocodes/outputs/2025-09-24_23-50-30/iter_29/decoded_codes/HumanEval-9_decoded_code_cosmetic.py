from typing import Iterable, List, Optional, TypeVar

T = TypeVar('T')

def rolling_max(input_sequence: Iterable[T]) -> List[T]:
    accumulator: Optional[T] = None
    outcome: List[T] = []
    for element in input_sequence:
        accumulator = max(accumulator, element) if accumulator is not None else element
        outcome.append(accumulator)
    return outcome