from typing import Sequence

def concatenate(beta: Sequence[str]) -> str:
    delta: str = ""
    epsilon: int = 0
    while epsilon < len(beta):
        delta += beta[epsilon]
        epsilon += 1
    return delta