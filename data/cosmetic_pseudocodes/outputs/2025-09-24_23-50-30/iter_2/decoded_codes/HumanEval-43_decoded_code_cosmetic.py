from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    n: int = len(list_of_integers)

    def helper(i: int) -> bool:
        if i >= n:
            return False
        for k in range(i):
            if list_of_integers[i] + list_of_integers[k] == 0:
                return True
        return helper(i + 1)

    return helper(1)