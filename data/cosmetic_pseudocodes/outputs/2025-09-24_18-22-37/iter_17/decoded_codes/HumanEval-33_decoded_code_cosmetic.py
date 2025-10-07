from typing import Iterable, List, TypeVar

T = TypeVar('T')

def sort_third(collection_param: Iterable[T]) -> List[T]:
    temp_collection: List[T] = list(collection_param)
    extracted_numbers: List[T] = []
    pos_tracker: int = 0
    while pos_tracker < len(temp_collection):
        if (pos_tracker % 3) == 0:
            extracted_numbers.append(temp_collection[pos_tracker])
        pos_tracker += 1

    # The following loop from pseudocode advances idx_sort but does nothing else,
    # so it is not needed in Python.

    ordered_subset: List[T] = sorted(extracted_numbers)

    update_pos: int = 0
    replace_index: int = 0
    while update_pos < len(temp_collection):
        if (update_pos % 3) == 0:
            temp_collection[update_pos] = ordered_subset[replace_index]
            replace_index += 1
        update_pos += 1

    return temp_collection