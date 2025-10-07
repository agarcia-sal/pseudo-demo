from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(sequence_container: Iterable[T]) -> List[T]:
    temp_container = set()
    accumulator: List[T] = []
    for element in sequence_container:
        if element not in temp_container:
            temp_container.add(element)
            accumulator.append(element)
    return sorted(accumulator)