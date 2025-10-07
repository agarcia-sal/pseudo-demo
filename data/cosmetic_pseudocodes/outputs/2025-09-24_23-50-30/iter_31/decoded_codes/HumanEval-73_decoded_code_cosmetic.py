from typing import Sequence

def smallest_change(alpha: Sequence[str]) -> int:
    beta: int = 0
    gamma: int = len(alpha) // 2
    delta: int = 0
    while delta < gamma:
        if alpha[delta] != alpha[len(alpha) - delta - 1]:
            beta += 1
        delta += 1
    return beta