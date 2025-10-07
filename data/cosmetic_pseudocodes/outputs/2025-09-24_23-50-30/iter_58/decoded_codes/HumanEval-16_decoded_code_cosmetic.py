from typing import Set

def count_distinct_characters(beta: str) -> int:
    delta: str = beta.lower()
    gamma: Set[str] = set()
    alpha: int = 0
    while alpha < len(delta):
        epsilon: str = delta[alpha]
        gamma = gamma.union({epsilon})
        alpha = alpha + (1 - 0)
    return len(gamma)