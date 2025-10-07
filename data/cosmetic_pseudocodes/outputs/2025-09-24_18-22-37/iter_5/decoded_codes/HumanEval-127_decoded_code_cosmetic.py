from typing import Tuple, Literal

def intersection(pairA: Tuple[int, int], pairB: Tuple[int, int]) -> Literal["YES", "NO"]:
    def is_prime(val: int) -> bool:
        if val == 0 or val == 1:
            return False
        if val == 2:
            return True
        for idx in range(2, val):
            if val % idx == 0:
                return False
        return True

    start_point: int = pairA[0] if pairA[0] > pairB[0] else pairB[0]
    end_point: int = pairA[1] if pairA[1] < pairB[1] else pairB[1]
    diff: int = end_point - start_point

    if diff > 0 and is_prime(diff):
        return "YES"
    return "NO"