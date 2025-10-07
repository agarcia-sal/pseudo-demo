from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    length: int = len(list_of_integers)
    for index_i in range(length - 1):
        element_i: int = list_of_integers[index_i]
        for index_j in range(index_i + 1, length):
            element_j: int = list_of_integers[index_j]
            if element_i + element_j == 0:
                return True
    return False