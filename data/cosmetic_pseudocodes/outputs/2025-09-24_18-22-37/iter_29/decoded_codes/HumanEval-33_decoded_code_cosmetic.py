from typing import Iterable, List, TypeVar

T = TypeVar('T')


def sort_third(data_collection: Iterable[T]) -> List[T]:
    copy_of_data: List[T] = list(data_collection)
    divisible_indices_values: List[T] = []
    idx_tracker: int = 0

    while idx_tracker < len(copy_of_data):
        if idx_tracker % 3 == 0:
            divisible_indices_values.append(copy_of_data[idx_tracker])
        idx_tracker += 1

    ordered_values = sorted(divisible_indices_values)

    replace_idx = 0
    substitute_pos = 0

    while replace_idx < len(copy_of_data):
        if replace_idx % 3 == 0:
            copy_of_data[replace_idx] = ordered_values[substitute_pos]
            substitute_pos += 1
        replace_idx += 1

    return copy_of_data