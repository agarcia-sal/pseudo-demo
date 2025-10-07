from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    pointer_a: int = 0
    length: int = len(list_of_integers)
    while pointer_a < length - 1:
        pointer_b: int = pointer_a + 1
        while pointer_b < length:
            if list_of_integers[pointer_a] + list_of_integers[pointer_b] == 0:
                return True
            pointer_b += 1
        pointer_a += 1
    return False