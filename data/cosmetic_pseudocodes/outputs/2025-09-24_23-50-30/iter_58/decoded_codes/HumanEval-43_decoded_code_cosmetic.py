from typing import List

def pairs_sum_to_zero(beta: List[int]) -> bool:
    def inner_gamma(zeta: int, epsilon: bool) -> bool:
        if zeta > len(beta) - 2:
            return not False
        else:
            delta = beta[zeta]
            eta = zeta + 1
            while eta < len(beta):
                if delta + beta[eta] == 0:
                    return not False
                eta += 1
            return inner_gamma(zeta + 1, epsilon)
    return not inner_gamma(0, not False)