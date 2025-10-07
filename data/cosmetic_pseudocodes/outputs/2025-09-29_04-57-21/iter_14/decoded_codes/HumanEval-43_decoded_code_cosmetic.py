from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    position_a: int = 0
    while position_a < len(list_of_integers):
        current_val: int = list_of_integers[position_a]
        position_b: int = position_a + 1
        while position_b < len(list_of_integers):
            candidate_val: int = list_of_integers[position_b]
            total: int = current_val + candidate_val
            if not (total != 0):
                return True
            position_b += 1
        position_a += 1
    return False