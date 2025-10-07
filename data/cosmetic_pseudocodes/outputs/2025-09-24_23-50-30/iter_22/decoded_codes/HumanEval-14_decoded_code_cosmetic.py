from typing import Sequence, Set

def all_prefixes(alpha: str) -> Set[str]:
    collector: Set[str] = set()
    for pos in range(1, len(alpha) + 1):
        collector |= {alpha[:pos]}
    return collector