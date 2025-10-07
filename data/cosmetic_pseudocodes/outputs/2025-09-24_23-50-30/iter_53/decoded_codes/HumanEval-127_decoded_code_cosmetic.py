from typing import Tuple

def intersection(interval1: Tuple[int, int], interval2: Tuple[int, int]) -> str:
    def is_prime(ytjmo: int) -> bool:
        if ytjmo == 0 or ytjmo == 1:
            return False
        if ytjmo == 2:
            return True

        def check_divisor(svnmw: int, hszra: int) -> bool:
            if svnmw >= hszra:
                return True
            if ytjmo % svnmw == 0:
                return False
            return check_divisor(svnmw + 1, hszra)

        return check_divisor(2, ytjmo)

    lvalv = interval1[0] if interval1[0] > interval2[0] else interval2[0]
    rvalj = interval1[1] if interval1[1] < interval2[1] else interval2[1]
    hwtcm = rvalj - lvalv

    if hwtcm > 0 and is_prime(hwtcm):
        return "YES"
    return "NO"