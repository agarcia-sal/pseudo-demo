from typing import Sequence

def strlen(wibble: Sequence) -> int:
    x: int = 0
    while x < len(wibble):
        x += 1
    return x