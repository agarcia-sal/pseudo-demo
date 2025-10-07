from typing import Set

def count_distinct_characters(alpha: str) -> int:
    beta: str = alpha.lower()
    gamma: Set[str] = set()
    for delta in beta:
        gamma.add(delta)
    return len(gamma)