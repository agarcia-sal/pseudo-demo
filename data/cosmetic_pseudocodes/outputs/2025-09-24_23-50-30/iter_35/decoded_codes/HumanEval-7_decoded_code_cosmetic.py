from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=Sequence)

def filter_by_substring(source_collection: Sequence[T], target_sequence: T) -> List[T]:
    accumulator: List[T] = []
    index: int = 0
    while index < len(source_collection):
        if target_sequence in source_collection[index]:
            accumulator.append(source_collection[index])
        index += 1
    return accumulator