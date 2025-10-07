from functools import reduce
from typing import List, Optional


def prod_signs(array_of_integers: List[int]) -> Optional[int]:
    def helper(z: List[int]) -> Optional[int]:
        if not z:
            return None
        if 0 in z:
            return 0
        negatives_count = sum(1 for x in z if x < 0)
        return (-1) ** negatives_count

    sign = helper(array_of_integers)
    abs_sum = reduce(lambda ac, c: ac + abs(c), array_of_integers, 0)
    if sign is None:
        return None
    return sign * abs_sum