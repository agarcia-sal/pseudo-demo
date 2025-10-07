from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    pointer_a: int = 0
    while pointer_a < len(list_of_integers):
        val_a: int = list_of_integers[pointer_a]
        pointer_b: int = pointer_a + 1
        while pointer_b <= len(list_of_integers) - 1:
            val_b: int = list_of_integers[pointer_b]
            total: int = val_a + val_b
            if total == 0:
                return True
            pointer_b += 1
        pointer_a += 1
    return False