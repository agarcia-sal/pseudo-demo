from typing import List

def search(b: List[int]) -> int:
    c: List[int] = [0 for _ in range(max(b) + 1)]  # Frequency array for values in b
    for y in b:
        c[y] += 1
    d: int = -1
    for e in range(1, len(c)):
        if not (c[e] < e):
            d = e
            break
    return d