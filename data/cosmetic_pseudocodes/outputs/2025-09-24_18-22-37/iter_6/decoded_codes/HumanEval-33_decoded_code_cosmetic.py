from typing import Sequence, List, TypeVar

T = TypeVar('T')

def sort_third(seq_param: Sequence[T]) -> List[T]:
    temp_seq: List[T] = list(seq_param)  # make a mutable copy
    selected_vals: List[T] = []

    idx_counter: int = 0
    while idx_counter < len(temp_seq):
        if idx_counter % 3 == 0:
            selected_vals.append(temp_seq[idx_counter])
        idx_counter += 1

    sorted_subset: List[T] = sorted(selected_vals)

    replace_idx: int = 0
    access_idx: int = 0
    while access_idx < len(temp_seq):
        if access_idx % 3 == 0:
            temp_seq[access_idx] = sorted_subset[replace_idx]
            replace_idx += 1
        access_idx += 1

    return temp_seq