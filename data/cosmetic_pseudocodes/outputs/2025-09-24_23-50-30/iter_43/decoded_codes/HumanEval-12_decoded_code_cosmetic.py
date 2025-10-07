from typing import List, Optional

def longest(alpha: List[str]) -> Optional[str]:
    if alpha:
        beta: int = 0
        for gamma in alpha:
            if len(gamma) > beta:
                beta = len(gamma)
        delta: int = 0
        while delta < len(alpha):
            if len(alpha[delta]) == beta:
                return alpha[delta]
            delta += 1
    else:
        return None