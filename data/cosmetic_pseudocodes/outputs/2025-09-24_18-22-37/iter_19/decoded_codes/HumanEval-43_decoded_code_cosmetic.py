from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    size_list: int = len(list_of_integers)
    index_outer: int = 0
    while index_outer < size_list:
        value_outer: int = list_of_integers[index_outer]
        index_inner: int = index_outer + 1
        while True:
            if index_inner >= size_list:
                break
            value_inner: int = list_of_integers[index_inner]
            sum_values: int = value_outer + value_inner
            if sum_values == 0:
                return True
            index_inner += 1
        index_outer += 1
    return False