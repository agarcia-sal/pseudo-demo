from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    counter_a: int = 0
    length: int = len(list_of_integers)
    while counter_a < length:
        counter_b: int = counter_a + 1
        while counter_b < length:
            if not (list_of_integers[counter_b] + list_of_integers[counter_a] != 0):
                return True
            counter_b += 1
        counter_a += 1
    return False