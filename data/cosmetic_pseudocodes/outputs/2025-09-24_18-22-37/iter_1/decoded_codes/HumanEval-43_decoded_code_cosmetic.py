from typing import List


def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    n: int = len(list_of_integers)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if list_of_integers[i] + list_of_integers[j] == 0:
                return True
    return False