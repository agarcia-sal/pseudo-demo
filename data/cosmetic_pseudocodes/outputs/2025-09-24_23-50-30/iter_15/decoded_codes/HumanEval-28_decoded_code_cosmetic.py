from typing import Sequence

def concatenate(beta: Sequence[str]) -> str:
    gamma: str = ""
    delta: int = 0
    while delta < len(beta):
        gamma += beta[delta]
        delta += 1
    return gamma