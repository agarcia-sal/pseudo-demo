from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    counter_alpha: int = 0
    n: int = len(list_of_integers)
    while counter_alpha < n:
        beta_index: int = counter_alpha + 1
        while beta_index < n:
            value_gamma: int = list_of_integers[counter_alpha]
            value_delta: int = list_of_integers[beta_index]
            sum_epsilon: int = value_gamma + value_delta
            if sum_epsilon == 0:
                return True
            beta_index += 1
        counter_alpha += 1
    return False