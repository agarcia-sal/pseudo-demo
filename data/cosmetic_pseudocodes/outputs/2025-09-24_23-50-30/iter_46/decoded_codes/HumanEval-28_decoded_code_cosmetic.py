from typing import Sequence

def concatenate(alpha: Sequence[str]) -> str:
    def helper(beta: Sequence[str], gamma: str) -> str:
        if not beta:
            return gamma
        else:
            return helper(beta[1:], gamma + beta[0])
    return helper(alpha, "")