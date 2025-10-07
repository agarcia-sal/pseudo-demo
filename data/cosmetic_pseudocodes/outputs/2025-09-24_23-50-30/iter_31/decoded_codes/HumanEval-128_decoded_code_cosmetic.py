from functools import reduce
from typing import List, Optional


def prod_signs(beta: List[int]) -> Optional[int]:
    if not beta:
        return None
    if 0 in beta:
        delta = 0
    else:
        kappa = sum(1 for x in beta if x < 0)
        delta = (-1) ** kappa
    omega = reduce(lambda acc, e: acc + abs(e), beta, 0)
    return delta * omega