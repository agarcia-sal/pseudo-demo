from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    found_flag: bool = False
    outer_index: int = 0
    n: int = len(list_of_integers)

    while outer_index < n and not found_flag:
        current_element: int = list_of_integers[outer_index]
        inner_index: int = outer_index + 1

        while inner_index < n:
            sum_elements: int = current_element + list_of_integers[inner_index]

            if sum_elements == 0:
                found_flag = True
                break

            if found_flag:
                break

            inner_index += 1

        outer_index += 1

    return found_flag