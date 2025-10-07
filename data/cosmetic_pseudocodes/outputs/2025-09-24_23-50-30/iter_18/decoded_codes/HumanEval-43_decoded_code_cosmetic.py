from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    len_vals = len(list_of_integers)

    counter_outer = 0
    while counter_outer < len_vals:
        current_element = list_of_integers[counter_outer]

        counter_inner = counter_outer + 1
        while counter_inner < len_vals:
            inner_element = list_of_integers[counter_inner]
            sum_elements = current_element + inner_element
            if sum_elements == 0:
                return True
            counter_inner += 1

        counter_outer += 1

    return False