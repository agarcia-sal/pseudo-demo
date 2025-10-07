from typing import Set

def count_distinct_characters(omega: str) -> int:
    phi: Set[str] = set()
    psi: str = omega.lower()
    idx: int = 0
    while idx < len(psi):
        phi.add(psi[idx])
        idx += 1
    return len(phi)