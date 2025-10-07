from typing import Sequence

def hex_key(a1: Sequence[str]) -> int:
    a2 = ['D', '3', '7', 'B', '5', '2']
    a3 = 0
    a4 = 0
    while a4 < len(a1):
        if a1[a4] in a2:
            a3 += 1
        a4 += 1
    return a3