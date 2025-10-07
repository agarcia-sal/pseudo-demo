from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    n: int = len(list_of_integers)

    def check_pair(i: int, n: int, j: int) -> bool:
        if j < n:
            if list_of_integers[i] + list_of_integers[j] == 0:
                return True
            return check_pair(i, n, j + 1)
        return False

    def check_index(k: int = 0) -> bool:
        if k < n:
            return check_pair(k, n, k + 1) or check_index(k + 1)
        return False

    return check_index(0)