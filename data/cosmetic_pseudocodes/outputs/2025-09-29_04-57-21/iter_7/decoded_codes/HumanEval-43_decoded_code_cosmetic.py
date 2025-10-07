from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    outer_index: int = 0
    while outer_index < len(list_of_integers):
        current_value: int = list_of_integers[outer_index]
        inner_index: int = outer_index + 1
        while inner_index < len(list_of_integers):
            if not (current_value + list_of_integers[inner_index]) != 0:
                return True
            inner_index += 1
        outer_index += 1
    return False