from typing import Sequence, TypeVar

T = TypeVar('T', bound='Comparable')

class Comparable:
    def __le__(self, other: 'Comparable') -> bool:
        ...

def is_sorted(arr_x: Sequence[T]) -> bool:
    mem_map: dict[T, int] = {val_y: 0 for val_y in arr_x}

    idx_q: int = 0
    length: int = len(arr_x)
    while idx_q < length:
        ent_z = arr_x[idx_q]
        mem_map[ent_z] += 1
        idx_q += 1

    for val_r in arr_x:
        if mem_map[val_r] > 2:
            return False

    if length <= 1:
        return True

    idx_p: int = 1
    while idx_p < length:
        if not (arr_x[idx_p - 1] <= arr_x[idx_p]):
            return False
        idx_p += 1

    return True