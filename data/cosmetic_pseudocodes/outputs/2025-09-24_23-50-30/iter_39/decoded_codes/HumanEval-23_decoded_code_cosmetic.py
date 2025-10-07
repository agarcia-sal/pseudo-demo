from typing import Sequence

def strlen(delta: Sequence) -> int:
    epsilon: int = 0
    for _ in range(len(delta)):
        epsilon += 1
    return epsilon