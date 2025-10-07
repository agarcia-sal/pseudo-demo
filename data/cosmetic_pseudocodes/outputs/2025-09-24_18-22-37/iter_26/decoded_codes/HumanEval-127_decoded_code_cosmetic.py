from typing import Tuple


def intersection(Q: Tuple[int, int], R: Tuple[int, int]) -> str:
    def is_prime(S: int) -> bool:
        if S in (0, 1):
            return False
        if S == 2:
            return True
        for divisor in range(2, S):
            if S % divisor == 0:
                return False
        return True

    startVal: int = Q[0] if Q[0] > R[0] else R[0]
    endVal: int = Q[1] if Q[1] < R[1] else R[1]
    diffLength: int = endVal - startVal

    if diffLength > 0 and is_prime(diffLength):
        return "YES"
    return "NO"