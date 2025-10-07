from typing import List, Sequence, TypeVar

T = TypeVar('T')

def sort_even(a_collection: Sequence[T]) -> List[T]:
    first_subset: List[T] = []
    second_subset: List[T] = []
    position: int = 0

    while position < len(a_collection):
        if position % 2 == 0:
            first_subset.append(a_collection[position])
        else:
            second_subset.append(a_collection[position])
        position += 1

    first_subset.sort()  # sort in non-decreasing order

    combined_result: List[T] = []
    idx_first: int = 0
    idx_second: int = 0

    while True:
        if idx_first >= len(first_subset):
            break
        combined_result.append(first_subset[idx_first])
        idx_first += 1
        if idx_second >= len(second_subset):
            break
        combined_result.append(second_subset[idx_second])
        idx_second += 1

    return combined_result