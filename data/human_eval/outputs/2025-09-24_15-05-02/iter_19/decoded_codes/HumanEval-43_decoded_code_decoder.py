from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    length: int = len(list_of_integers)
    for index_i, element_i in enumerate(list_of_integers):
        for index_j in range(index_i + 1, length):
            if element_i + list_of_integers[index_j] == 0:
                return True
    return False