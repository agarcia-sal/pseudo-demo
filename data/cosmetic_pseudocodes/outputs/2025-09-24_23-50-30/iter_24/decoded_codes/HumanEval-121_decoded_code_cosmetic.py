from typing import List

def solution(alpha: List[int]) -> int:
    def accumulateBeta(gamma: List[int], delta: int, epsilon: int, zeta: int) -> int:
        if epsilon == len(gamma):
            return delta
        if not (epsilon % 2 == 1 and gamma[epsilon] % 2 == 0):
            return accumulateBeta(gamma, delta + gamma[epsilon], epsilon + 1, zeta)
        else:
            return accumulateBeta(gamma, delta, epsilon + 1, zeta)
    return accumulateBeta(alpha, 0, 0, 0)