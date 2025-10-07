from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    position_a: int = 0
    n: int = len(list_of_integers)
    while position_a < n:
        position_b: int = position_a + 1
        while position_b < n:
            if list_of_integers[position_b] == -list_of_integers[position_a]:
                return True
            position_b += 1
        position_a += 1
    return False