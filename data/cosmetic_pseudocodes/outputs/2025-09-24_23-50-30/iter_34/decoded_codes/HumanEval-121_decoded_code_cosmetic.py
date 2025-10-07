from typing import List


def solution(alpha: List[int]) -> int:
    def beta(gamma: List[int], delta: int) -> int:
        if delta < 0:
            return 0
        current = gamma[delta] if (gamma[delta] % 2 == 1 and delta % 2 == 0) else 0
        return current + beta(gamma, delta - 1)
    return beta(alpha, len(alpha) - 1)