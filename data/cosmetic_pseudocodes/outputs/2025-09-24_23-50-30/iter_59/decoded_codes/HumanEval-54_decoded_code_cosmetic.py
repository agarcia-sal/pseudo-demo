from typing import Iterable

def same_chars(alp0: Iterable[str], alp1: Iterable[str]) -> bool:
    b2 = set(alp0)
    c3 = set(alp1)
    return b2 == c3