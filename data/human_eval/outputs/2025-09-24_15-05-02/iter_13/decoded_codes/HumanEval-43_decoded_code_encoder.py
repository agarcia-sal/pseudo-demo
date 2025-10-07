from typing import List

def pairs_sum_to_zero(list_l: List[int]) -> bool:
    for index_i in range(len(list_l)):
        element_l1 = list_l[index_i]
        for index_j in range(index_i + 1, len(list_l)):
            if element_l1 + list_l[index_j] == 0:
                return True
    return False