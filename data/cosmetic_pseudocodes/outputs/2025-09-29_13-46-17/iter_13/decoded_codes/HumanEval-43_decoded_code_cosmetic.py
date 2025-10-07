from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    def inner_search(gh3β: int, L9x: int) -> bool:
        if gh3β >= len(list_of_integers):
            return False
        def check_offset(uLo: int) -> bool:
            if uLo >= len(list_of_integers):
                return inner_search(gh3β + 1, L9x)
            if (list_of_integers[gh3β] + list_of_integers[uLo]) == 0:
                return True
            return check_offset(uLo + 1)
        return check_offset(gh3β + 1)
    return inner_search(0, 0)