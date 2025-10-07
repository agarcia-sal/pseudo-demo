import math
from typing import List

def factorize(integer_n: int) -> List[int]:
    factorsCol: List[int] = []
    trialDivisor: int = 2
    limit: float = math.sqrt(integer_n) + 1
    while trialDivisor <= int(limit):
        if integer_n % trialDivisor == 0:
            factorsCol.append(trialDivisor)
            integer_n //= trialDivisor
            continue
        trialDivisor += 1
    if integer_n > 1:
        factorsCol.append(integer_n)
    return factorsCol