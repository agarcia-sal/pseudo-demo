from typing import List
import math

def factorize(integer_n: int) -> List[int]:
    list_of_factors: List[int] = []
    if integer_n <= 1:
        return list_of_factors
    i = 2
    while i <= int(math.isqrt(integer_n)) + 1:
        if integer_n % i == 0:
            list_of_factors.append(i)
            integer_n //= i
        else:
            i += 1
    if integer_n > 1:
        list_of_factors.append(integer_n)
    return list_of_factors