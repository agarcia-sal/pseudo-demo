from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    outer_counter: int = 0
    n: int = len(list_of_integers)
    while outer_counter < n:
        current_value: int = list_of_integers[outer_counter]
        inner_counter: int = outer_counter
        while inner_counter < n - 1:
            inner_counter += 1
            sum_result: int = current_value + list_of_integers[inner_counter]
            if sum_result == 0:
                return True
        outer_counter += 1
    return False