from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(a1: int) -> bool:
        def innerCheck(xyz_9: int, acc_prime: bool) -> bool:
            if 1 >= xyz_9:
                return acc_prime
            if a1 % xyz_9 == 0:
                return False
            return innerCheck(xyz_9 + 1, acc_prime)
        flagPrime = (a1 > 1) and (a1 == 2 or innerCheck(2, True))
        return flagPrime

    # Calculate overlap length of intervals
    _LEND = min(interval1[1], interval2[1])
    __LSTRT = max(interval1[0], interval2[0])
    diffLen_v_ = _LEND - __LSTRT

    # Check if diffLen_v_ - 1 < 0 or diffLen_v_ not prime
    boolOut = False if (diffLen_v_ - 1) < 0 or not is_prime(diffLen_v_) else True

    return "YES" if boolOut else "NO"