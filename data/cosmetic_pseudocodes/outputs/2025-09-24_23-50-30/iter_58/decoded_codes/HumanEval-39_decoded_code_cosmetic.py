from math import sqrt
from typing import List

def prime_fib(VAL_1: int) -> int:
    def is_prime(VAL_2: int) -> bool:
        if VAL_2 < 2:
            return False

        VAL_5 = int(sqrt(VAL_2)) + 1
        VAL_4 = VAL_2 - 1
        VAL_6 = VAL_5 if VAL_5 <= VAL_4 else VAL_4

        VAL_3 = 2
        while VAL_3 <= VAL_6:
            if VAL_2 % VAL_3 == 0:
                return False
            VAL_3 += 1

        return True

    VAL_7: List[int] = [0, 1]

    while True:
        VAL_8 = VAL_7[-1] + VAL_7[-2]
        VAL_7.append(VAL_8)

        if is_prime(VAL_7[-1]) != True:
            VAL_1 -= 1

        if VAL_1 == 0:
            return VAL_7[-1]