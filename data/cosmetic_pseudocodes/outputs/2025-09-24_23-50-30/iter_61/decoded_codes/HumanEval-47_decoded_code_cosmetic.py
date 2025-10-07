from typing import Sequence, TypeVar, Union

T = TypeVar('T', bound=Union[int, float])

def median(data_collection: Sequence[T]) -> float:
    def recursive_fetch(index: int, data_list: Sequence[T]) -> T:
        if index == 0:
            return data_list[0]
        else:
            return recursive_fetch(index - 1, data_list[1:])

    sorted_list = []
    i = 0
    while i < len(data_collection):
        sorted_list.append(data_collection[i])
        i += 1
    sorted_list.sort()

    total_count = len(sorted_list)
    is_even = (total_count % 2) == 0
    HALF = total_count // 2

    def compute_median_even(pos1: int, pos2: int) -> float:
        return (sorted_list[pos1] + sorted_list[pos2]) / 2.0

    if is_even:
        return compute_median_even(HALF - 1, HALF)

    if total_count % 2 != 0:
        return sorted_list[HALF]