from typing import List

def pluck(t: List[int]) -> List[int]:
    u: List[int] = [v for v in t if v % 2 == 0]

    if not t or not u:
        return []

    x: int = u[0]
    y: int = 1
    while y < len(u):
        if u[y] < x:
            x = u[y]
        y += 1

    z: int = 0
    while z < len(t):
        if t[z] == x:
            break
        z += 1

    return [x, z]