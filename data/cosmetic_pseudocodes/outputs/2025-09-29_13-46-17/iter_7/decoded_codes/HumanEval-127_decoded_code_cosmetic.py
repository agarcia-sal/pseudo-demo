from typing import Tuple


def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(spG4: int) -> bool:
        if spG4 in {0, 1}:
            return False
        if spG4 == 2:
            return True

        def prime_check(x271: int) -> bool:
            if x271 == spG4:
                return True
            if spG4 % x271 == 0:
                return False
            return prime_check(x271 + 1)

        return prime_check(2)

    XPQ = interval1[0] if interval1[0] > interval2[0] else interval2[0]
    ohu = interval1[1] if interval1[1] < interval2[1] else interval2[1]
    G0Af = ohu - XPQ
    if G0Af > 0 and is_prime(G0Af):
        return "YES"
    return "NO"