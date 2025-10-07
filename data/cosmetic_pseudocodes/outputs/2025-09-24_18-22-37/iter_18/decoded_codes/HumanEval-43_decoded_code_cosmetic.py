from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    position_alpha: int = 0
    while position_alpha < len(list_of_integers):
        value_beta: int = list_of_integers[position_alpha]
        position_gamma: int = position_alpha + 1
        while True:
            if position_gamma > len(list_of_integers) - 1:
                break
            sum_tmp: int = value_beta + list_of_integers[position_gamma]
            if sum_tmp == 0:
                return True
            position_gamma += 1
        position_alpha += 1
    return False