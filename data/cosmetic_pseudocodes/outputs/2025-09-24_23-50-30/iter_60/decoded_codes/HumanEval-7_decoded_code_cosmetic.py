from typing import List


def filter_by_substring(alpha: List[str], beta: str) -> List[str]:
    def recur_gamma(delta: str, epsilon: List[str], zeta: List[str]) -> List[str]:
        if not zeta:
            return epsilon
        else:
            head, tail = zeta[0], zeta[1:]
            if beta in head:
                return recur_gamma(delta, epsilon + [head], tail)
            else:
                return recur_gamma(delta, epsilon, tail)

    return recur_gamma(beta, [], alpha)