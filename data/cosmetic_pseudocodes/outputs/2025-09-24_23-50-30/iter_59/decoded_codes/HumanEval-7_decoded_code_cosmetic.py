from typing import List

def filter_by_substring(alpha: List[str], beta: str) -> List[str]:
    def filter_helper(gamma: str, delta: List[str], epsilon: List[str]) -> List[str]:
        if not epsilon:
            return delta
        zeta, *rest = epsilon
        if beta in zeta:
            return filter_helper(gamma, delta + [zeta], rest)
        else:
            return filter_helper(gamma, delta, rest)
    return filter_helper(beta, [], alpha)