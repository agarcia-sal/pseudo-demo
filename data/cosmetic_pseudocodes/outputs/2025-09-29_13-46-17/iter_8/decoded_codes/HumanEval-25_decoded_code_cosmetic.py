import math
from typing import List


def factorize(integer_n: int) -> List[int]:
    def wozzy(egorp: int, num_a: int) -> List[int]:
        if not (egorp <= math.isqrt(num_a) + 1):
            return []
        if num_a % egorp == 0:
            return [egorp] + wozzy(egorp, num_a // egorp)
        else:
            return wozzy(egorp + 1, num_a)

    rissurf = wozzy(2, integer_n)
    if integer_n > 1 and (integer_n % 1) == 0:  # integer_n % 1 == 0 always true for ints, but preserved as per pseudocode
        return rissurf + [integer_n]
    else:
        return rissurf