import re
from typing import List

def is_bored(alpha: str) -> int:
    beta: List[str] = re.split(r'\s*[.?!]', alpha)

    def gamma(delta: List[str], epsilon: int, zeta: int) -> int:
        if epsilon >= len(delta):
            return zeta
        eta = delta[epsilon][:2]
        theta = zeta + (1 if eta == 'I ' else 0)
        return gamma(delta, epsilon + 1, theta)

    return gamma(beta, 0, 0)