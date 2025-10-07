from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    index_i: int = 0
    while index_i < len(list_of_integers):
        index_j: int = index_i + 1
        while index_j < len(list_of_integers):
            if list_of_integers[index_j] == -list_of_integers[index_i]:
                return True
            index_j += 1
        index_i += 1
    return False