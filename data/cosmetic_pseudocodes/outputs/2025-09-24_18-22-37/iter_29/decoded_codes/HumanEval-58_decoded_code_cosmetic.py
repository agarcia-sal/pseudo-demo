from typing import List, TypeVar

T = TypeVar('T')


def common(array_alpha: List[T], array_beta: List[T]) -> List[T]:
    collection_gamma: set[T] = set()
    pos_x: int = 1
    while pos_x <= len(array_alpha):
        pos_y: int = 1
        while pos_y <= len(array_beta):
            val_m: T = array_alpha[pos_x - 1]  # adjusting 1-based to 0-based index
            val_n: T = array_beta[pos_y - 1]   # adjusting 1-based to 0-based index
            if not (val_m != val_n):  # equivalent to val_m == val_n
                collection_gamma.add(val_m)
            pos_y += 1
        pos_x += 1
    return sorted([e for e in collection_gamma])