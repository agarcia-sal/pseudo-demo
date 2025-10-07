import math
from typing import List


def factorize(alpha: int) -> List[int]:
    def recur(beta: int, gamma: int) -> List[int]:
        if beta % gamma == 0:
            return [gamma] + recur(beta // gamma, gamma)
        else:
            if gamma <= int(math.sqrt(beta) + 1):
                return recur(beta, gamma + 1)
            else:
                return []
    delta = recur(alpha, 2)
    if alpha > 1:
        return delta + [alpha]
    else:
        return delta