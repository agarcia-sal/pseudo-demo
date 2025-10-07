from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    for position_a in range(len(list_of_integers) - 1):
        value_a = list_of_integers[position_a]
        position_b = position_a + 1
        while position_b < len(list_of_integers):
            value_b = list_of_integers[position_b]
            if value_a + value_b == 0:
                return True
            position_b += 1
    return False