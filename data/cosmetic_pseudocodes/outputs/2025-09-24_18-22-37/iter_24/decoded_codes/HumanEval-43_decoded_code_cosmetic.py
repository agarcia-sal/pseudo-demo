from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    flag_found: bool = False
    outer_counter: int = 0
    length: int = len(list_of_integers)
    while outer_counter < length:
        current_element: int = list_of_integers[outer_counter]
        inner_counter: int = outer_counter + 1
        if inner_counter < length:
            while inner_counter < length:
                compare_element: int = list_of_integers[inner_counter]
                sum_result: int = current_element + compare_element
                if sum_result == 0:
                    flag_found = True
                    break
                inner_counter += 1
        if flag_found:
            break
        outer_counter += 1
    return flag_found