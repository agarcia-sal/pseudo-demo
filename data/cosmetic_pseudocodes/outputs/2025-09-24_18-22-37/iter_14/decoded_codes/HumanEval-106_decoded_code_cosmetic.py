from typing import List

def f(alpha: int) -> List[int]:
    result: List[int] = []
    beta: int = 1
    while beta <= alpha:
        delta = beta % 2
        if delta == 0:
            gamma = 1
            epsilon = 1
            # Compute factorial of beta
            while epsilon <= beta:
                gamma *= epsilon
                epsilon += 1
            result.append(gamma)
        else:
            zeta = 0
            eta = 1
            # Compute sum of integers from 1 to beta
            while eta <= beta:
                zeta += eta
                eta += 1
            result.append(zeta)
        beta += 1
    return result