from typing import List

def all_prefixes(y: str) -> List[str]:
    z: List[str] = []
    a: int = 0
    while a <= len(y) - 1:
        b: int = a + 1
        c: str = y[:b]
        z.append(c)
        a += 1
    return z