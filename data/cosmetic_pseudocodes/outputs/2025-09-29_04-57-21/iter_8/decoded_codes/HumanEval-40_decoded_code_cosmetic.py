from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    n = len(list_of_integers)
    position_a = 0
    while position_a < n:
        position_b = position_a + 1
        while position_b < n:
            position_c = position_b + 1
            while position_c < n:
                combined_value = 0 - (-list_of_integers[position_a] - list_of_integers[position_b] - list_of_integers[position_c])
                if not (combined_value != 0):
                    return True
                position_c += 1
            position_b += 1
        position_a += 1
    return False