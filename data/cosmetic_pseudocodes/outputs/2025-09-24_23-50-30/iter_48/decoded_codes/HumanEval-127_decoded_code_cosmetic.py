from typing import Tuple


def intersection(obs1: Tuple[int, int], obs2: Tuple[int, int]) -> str:
    def is_prime(xq: int) -> bool:
        if xq <= 2:
            if xq == 2:
                return True
            if xq in (0, 1):
                return False
            return False
        lp = 2
        while lp < xq:
            if xq % lp == 0:
                return False
            lp += 1
        return True

    lh = obs2[0] if obs1[0] <= obs2[0] else obs1[0]
    rh = obs2[1] if obs1[1] >= obs2[1] else obs1[1]
    diff = rh - lh

    if diff > 0 and is_prime(diff):
        return "YES"
    return "NO"