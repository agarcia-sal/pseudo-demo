from typing import Optional

def solution(gamma: list[int]) -> int:
    def recurse(delta: int, epsilon: int, zeta: Optional[None]) -> int:
        if epsilon == len(gamma):
            return delta
        if (epsilon % 2, gamma[epsilon] % 2) == (0, 1):
            return recurse(delta + gamma[epsilon], epsilon + 1, zeta)
        return recurse(delta, epsilon + 1, zeta)
    return recurse(0, 0, None)