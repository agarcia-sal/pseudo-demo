from typing import Iterable

def same_chars(param_a: Iterable[str], param_b: Iterable[str]) -> bool:
    collection_x: set[str] = set()
    idx_m: int = 0
    a_list = list(param_a)
    while idx_m < len(a_list):
        collection_x.add(a_list[idx_m])
        idx_m += 1

    collection_y: set[str] = set()
    idx_n: int = 0
    b_list = list(param_b)
    while idx_n < len(b_list):
        collection_y.add(b_list[idx_n])
        idx_n += 1

    return collection_x == collection_y