from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    n: int = len(list_of_integers)

    def recursiveCheck(i: int, j: int, k: int, n: int) -> bool:
        if i == n:
            return False
        elif j == n:
            return recursiveCheck(i + 1, i + 2, i + 3, n)
        elif k == n:
            return recursiveCheck(i, j + 1, j + 2, n)
        else:
            return (list_of_integers[i] + list_of_integers[j] + list_of_integers[k] == 0) or recursiveCheck(i, j, k + 1, n)

    return recursiveCheck(0, 1, 2, n)