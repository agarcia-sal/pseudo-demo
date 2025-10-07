from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    seen = set()
    for number in list_of_integers:
        if -number in seen:
            return True
        seen.add(number)
    return False