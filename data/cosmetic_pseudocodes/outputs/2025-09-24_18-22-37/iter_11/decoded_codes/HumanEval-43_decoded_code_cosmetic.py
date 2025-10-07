from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    length_list: int = len(list_of_integers)
    index_outer: int = 0
    while index_outer < length_list:
        current_element: int = list_of_integers[index_outer]
        index_inner: int = index_outer + 1
        while index_inner < length_list:
            inner_element: int = list_of_integers[index_inner]
            if current_element + inner_element == 0:
                return True
            index_inner += 1
        index_outer += 1
    return False