from typing import List

def tri(alpha: int) -> List[float]:
    if alpha != 0:
        beta: List[float] = [1, 3]
        gamma: int = 2
        while gamma <= alpha:
            if gamma % 2 == 0:
                beta.append((gamma / 2) + 1)
            else:
                beta.append(beta[gamma - 1] + beta[gamma - 2] + ((gamma + 3) / 2))
            gamma += 1
        return beta
    else:
        return [1]