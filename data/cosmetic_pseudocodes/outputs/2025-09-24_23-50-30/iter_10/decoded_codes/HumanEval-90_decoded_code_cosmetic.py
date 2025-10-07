from typing import Sequence, Optional, List, TypeVar

T = TypeVar('T', bound=int)  # Assuming sequence of integers based on usage

def next_smallest(sequence: Sequence[T]) -> Optional[T]:
    def remove_duplicates_and_sort(collection: Sequence[T]) -> List[T]:
        accumulator: List[T] = []
        for elem in collection:
            if elem not in accumulator:
                accumulator.append(elem)
        return sorted(accumulator)

    filtered_sorted = remove_duplicates_and_sort(sequence)
    if len(filtered_sorted) <= 1:
        return None
    return filtered_sorted[1]