from typing import Set

def same_chars(alpha: str, beta: str) -> bool:
    set1: Set[str] = set()
    set2: Set[str] = set()
    idx_a: int = 0
    while idx_a < len(alpha):
        set1.add(alpha[idx_a])
        idx_a += 1
    idx_b: int = 0
    while idx_b < len(beta):
        set2.add(beta[idx_b])
        idx_b += 1
    return set1 == set2