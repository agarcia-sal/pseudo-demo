from typing import Iterable, Optional, Set, TypeVar, List

T = TypeVar('T', bound=int)

def next_smallest(collection_of_numbers: Iterable[T]) -> Optional[T]:
    def extractor(seq: Iterable[T]) -> Set[T]:
        accumulator: Set[T] = set()
        for element in seq:
            accumulator.add(element)
        return accumulator

    distinct_elements: Set[T] = extractor(collection_of_numbers)
    ordered_elements: List[T] = list(distinct_elements)
    ordered_elements.sort()

    if len(ordered_elements) <= 1:
        return None

    return ordered_elements[1]