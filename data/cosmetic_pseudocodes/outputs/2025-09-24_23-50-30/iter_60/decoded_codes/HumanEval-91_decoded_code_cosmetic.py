import re
from typing import List

def is_bored(alpha: str) -> int:
    def count_matches(beta: List[str], gamma: int, delta: int) -> int:
        if delta == len(beta):
            return gamma
        epsilon = beta[delta][:2] == 'I '
        return count_matches(beta, gamma + (1 if epsilon else 0), delta + 1)
    zeta = re.split(r'\s*[.?!]', alpha)
    eta = count_matches(zeta, 0, 0)
    return eta