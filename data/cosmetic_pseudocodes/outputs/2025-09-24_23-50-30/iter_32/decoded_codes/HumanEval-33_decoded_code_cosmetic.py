from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    arr_copy: List[T] = list_input[:]
    idx_seq: List[int] = [k for k in range(len(arr_copy)) if k % 3 == 0]
    extract_vals: List[T] = [arr_copy[m] for m in idx_seq]
    ordered_vals: List[T] = sorted(extract_vals)
    for i in range(len(idx_seq)):
        arr_copy[idx_seq[i]] = ordered_vals[i]
    return arr_copy