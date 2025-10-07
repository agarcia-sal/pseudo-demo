from typing import Sequence

def strlen(alpha: Sequence) -> int:
    beta: int = 0
    while True:
        if beta >= len(alpha):
            break
        beta += 1
    return beta