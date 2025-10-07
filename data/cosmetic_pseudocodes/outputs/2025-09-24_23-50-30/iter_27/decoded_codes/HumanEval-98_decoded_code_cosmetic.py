from typing import Sequence

def count_upper(w: Sequence[str]) -> int:
    v: int = 0
    z: int = 0
    while z < len(w):
        if w[z] in "AEIOU":
            v += 1
        z += 2
    return v