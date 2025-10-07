from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    outer_idx: int = 0
    length: int = len(list_of_integers)
    while outer_idx < length:
        first_val: int = list_of_integers[outer_idx]
        for inner_idx in range(outer_idx + 1, length):
            second_val: int = list_of_integers[inner_idx]
            combined: int = first_val + second_val
            if combined == 0:
                return True
        outer_idx += 1
    return False