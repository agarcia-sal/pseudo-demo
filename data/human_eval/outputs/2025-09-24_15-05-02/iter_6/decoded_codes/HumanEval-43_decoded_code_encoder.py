from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    for i in range(len(list_of_integers) - 1):
        first_element = list_of_integers[i]
        for j in range(i + 1, len(list_of_integers)):
            if first_element + list_of_integers[j] == 0:
                return True
    return False