from typing import Sequence

def concatenate(w: Sequence[str]) -> str:
    x: str = ""
    y: int = 0
    while y < len(w):
        x += w[y]
        y += 1
    return x