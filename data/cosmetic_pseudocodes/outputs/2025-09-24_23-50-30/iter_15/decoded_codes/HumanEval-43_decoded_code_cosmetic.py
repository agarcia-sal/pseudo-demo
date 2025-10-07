from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    length_m: int = len(list_of_integers)
    idx_a: int = 0

    while idx_a < length_m:
        idx_b: int = idx_a + 1

        while idx_b < length_m:
            val_x: int = list_of_integers[idx_a]
            val_y: int = list_of_integers[idx_b]

            if not (val_x + val_y) != 0:
                return True

            idx_b += 1

        idx_a += 1

    return False