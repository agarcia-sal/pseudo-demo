from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    def check_pairs(i: int) -> bool:
        if i >= len(list_of_integers):
            return False

        def check_j(j: int) -> bool:
            if j >= len(list_of_integers):
                return check_pairs(i + 1)
            if list_of_integers[i] + list_of_integers[j] == 0:
                return True
            return check_j(j + 1)

        return check_j(i + 1)

    return check_pairs(0)