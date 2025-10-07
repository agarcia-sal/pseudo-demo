from typing import Tuple

def intersection(delta0: Tuple[int, int], delta1: Tuple[int, int]) -> str:
    def is_prime(rho: int) -> bool:
        if rho in (0, 1):
            return False
        if rho == 2:
            return True
        for aux0 in range(2, rho):
            if rho % aux0 == 0:
                return False
        return True

    valA: int = delta0[0] if delta0[0] >= delta1[0] else delta1[0]
    valB: int = delta0[1] if delta0[1] < delta1[1] else delta1[1]
    span: int = valB - valA

    if span > 0 and is_prime(span):
        return "YES"
    else:
        return "NO"