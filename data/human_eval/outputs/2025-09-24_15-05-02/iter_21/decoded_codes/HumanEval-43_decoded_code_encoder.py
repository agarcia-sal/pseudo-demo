from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    length = len(list_of_integers)
    for i in range(length - 1):
        element_i = list_of_integers[i]
        for j in range(i + 1, length):
            if element_i + list_of_integers[j] == 0:
                return True
    return False