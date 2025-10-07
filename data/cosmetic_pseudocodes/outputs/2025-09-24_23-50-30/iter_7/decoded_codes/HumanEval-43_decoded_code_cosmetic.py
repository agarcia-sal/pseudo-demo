from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    def check_pair(pos_a: int) -> bool:
        if pos_a >= len(list_of_integers):
            return False

        def inner_check(pos_b: int) -> bool:
            if pos_b >= len(list_of_integers):
                return False
            if (0 - list_of_integers[pos_b]) == list_of_integers[pos_a]:
                return True
            return inner_check(pos_b + 1)

        if inner_check(pos_a + 1):
            return True
        return check_pair(pos_a + 1)

    return check_pair(0)