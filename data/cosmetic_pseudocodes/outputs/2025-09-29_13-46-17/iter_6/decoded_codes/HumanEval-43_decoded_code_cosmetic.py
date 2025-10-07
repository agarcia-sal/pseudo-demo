from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    n_total: int = len(list_of_integers)

    def recursive_check(curr_pos: int, next_pos: int) -> bool:
        if curr_pos >= n_total:
            return False
        if next_pos >= n_total:
            return recursive_check(curr_pos + 1, curr_pos + 2)
        val_a: int = list_of_integers[curr_pos]
        val_b: int = list_of_integers[next_pos]
        if val_a + val_b == 0:
            return True
        return recursive_check(curr_pos, next_pos + 1)

    return recursive_check(0, 1)