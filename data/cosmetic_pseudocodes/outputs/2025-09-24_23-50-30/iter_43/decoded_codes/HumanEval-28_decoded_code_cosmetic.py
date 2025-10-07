from typing import Sequence

def concatenate(c_alpha: Sequence[str]) -> str:
    c_bravo: str = ""
    c_charlie: int = 0
    while c_charlie < len(c_alpha):
        c_bravo += c_alpha[c_charlie]
        c_charlie += 1
    return c_bravo