from typing import List

def all_prefixes(delta: str) -> List[str]:
    omega: List[str] = []
    ll: int = len(delta)
    mu: int = 0
    while mu < ll:
        chi: str = delta[:mu + 1]
        omega.append(chi)
        mu += 1
    return omega