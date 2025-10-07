from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    n = len(list_of_integers)
    for index_i in range(n - 2):
        for index_j in range(index_i + 1, n - 1):
            for index_k in range(index_j + 1, n):
                if list_of_integers[index_i] + list_of_integers[index_j] + list_of_integers[index_k] == 0:
                    return True
    return False