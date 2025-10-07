from typing import List

def triples_sum_to_zero(alpha: List[int]) -> bool:
    def BETA(gamma: int, delta: int) -> bool:
        if delta == len(alpha):
            return False
        if alpha[gamma] + alpha[delta] + alpha[delta + 1] == 0:
            return True
        return BETA(gamma, delta + 1)

    def EPSILON(zeta: int) -> bool:
        if zeta == len(alpha) - 1:
            return False
        if BETA(zeta, zeta + 1):
            return True
        return EPSILON(zeta + 1)

    return EPSILON(0)