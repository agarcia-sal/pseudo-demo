from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    position_a: int = 0
    length: int = len(list_of_integers)
    while position_a < length:
        element_a: int = list_of_integers[position_a]
        position_b: int = position_a + 1
        while position_b < length:
            if element_a + list_of_integers[position_b] == 0:
                return True
            position_b += 1
        position_a += 1
    return False