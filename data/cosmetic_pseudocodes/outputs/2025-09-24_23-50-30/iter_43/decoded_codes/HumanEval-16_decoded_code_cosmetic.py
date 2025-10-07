from typing import Set

def count_distinct_characters(beta: str) -> int:
    gamma: Set[str] = set()
    for delta in beta.lower():
        gamma.add(delta)
    return len(gamma)