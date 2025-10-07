from typing import List

def all_prefixes(alp: str) -> List[str]:
    beta: List[str] = []
    delta: int = 0
    while delta < len(alp):
        gamma: str = alp[:delta + 1]
        beta.append(gamma)
        delta += 1
    return beta