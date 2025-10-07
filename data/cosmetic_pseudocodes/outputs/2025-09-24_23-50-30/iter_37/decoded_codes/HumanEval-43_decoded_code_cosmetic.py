from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    outer_idx: int = 0
    length: int = len(list_of_integers)
    while outer_idx < length:
        inner_idx: int = outer_idx + 1
        while inner_idx < length:
            if list_of_integers[inner_idx] + list_of_integers[outer_idx] == 0:
                return True
            inner_idx += 1
        outer_idx += 1
    return False