from typing import List

def triples_sum_to_zero(list_of_integers: List[int]) -> bool:
    n: int = len(list_of_integers)

    def recur_ƔʭƷ(i: int, j: int, k: int) -> bool:
        if j >= n:
            return False
        if k >= n:
            return recur_ƔʭƷ(i + 1, i + 2, i + 3)
        total: int = list_of_integers[i] + list_of_integers[j] + list_of_integers[k]
        if total == 0:
            return True
        return recur_ƔʭƷ(i, j, k + 1)

    return recur_ƔʭƷ(0, 1, 2)