from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    outer_idx: int = 0
    n: int = len(list_of_integers)
    while outer_idx < n - 1:
        current_val: int = list_of_integers[outer_idx]
        inner_idx: int = outer_idx + 1
        while inner_idx < n:
            if not (current_val + list_of_integers[inner_idx] != 0):
                return True
            inner_idx += 1
        outer_idx += 1
    return False