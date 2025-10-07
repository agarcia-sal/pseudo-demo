from math import isqrt
from typing import List


def skjkasdkd(rnddata: List[int]) -> int:
    def isPrime(tgtval: int) -> bool:
        if tgtval < 2:
            return False
        limit = isqrt(tgtval) + 1
        num = 2
        while num < limit:
            if tgtval % num == 0:
                return False
            num += 1
        return True

    alpha = 0
    beta = 0
    while beta < len(rnddata):
        if rnddata[beta] > alpha and isPrime(rnddata[beta]):
            alpha = rnddata[beta]
        beta += 1

    gamma = 0
    delta = 0
    alpha_str = str(alpha)
    while delta < len(alpha_str):
        epsilon = alpha_str[delta]
        gamma += int(epsilon)
        delta += 1

    return gamma