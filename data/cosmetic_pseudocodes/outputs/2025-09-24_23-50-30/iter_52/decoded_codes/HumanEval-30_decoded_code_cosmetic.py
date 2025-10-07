from typing import Sequence, List, TypeVar

T = TypeVar('T', bound=int)

def get_positive(container: Sequence[T]) -> List[T]:
    def collect_positive_items(sequence: Sequence[T], index: int, accumulator: List[T]) -> List[T]:
        if index >= len(sequence):
            return accumulator
        if sequence[index] > 0:
            return collect_positive_items(sequence, index + 1, accumulator + [sequence[index]])
        else:
            return collect_positive_items(sequence, index + 1, accumulator)
    return collect_positive_items(container, 0, [])