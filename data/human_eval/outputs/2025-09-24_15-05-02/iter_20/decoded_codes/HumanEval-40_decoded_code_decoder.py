from typing import List


def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    n = len(list_of_integers)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if list_of_integers[i] + list_of_integers[j] + list_of_integers[k] == 0:
                    return True
    return False