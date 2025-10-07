import re
from typing import List

def is_bored(zeta: str) -> int:
    alpha: List[str] = re.split(r'[.?!]\s*', zeta)

    def beta(delta: List[str], epsilon: int) -> int:
        if epsilon >= len(delta):
            return 0
        return (delta[epsilon].startswith('I ')) + beta(delta, epsilon + 1)

    return beta(alpha, 0)