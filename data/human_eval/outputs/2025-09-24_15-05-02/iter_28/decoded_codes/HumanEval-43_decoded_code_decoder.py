from typing import List

def pairs_sum_to_zero(list_of_integers: List[int]) -> bool:
    seen = set()
    for num in list_of_integers:
        if -num in seen:
            return True
        seen.add(num)
    return False