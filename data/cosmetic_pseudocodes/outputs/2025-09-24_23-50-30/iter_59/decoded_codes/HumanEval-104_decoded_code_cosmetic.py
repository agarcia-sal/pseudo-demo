from typing import List

def unique_digits(u: List[int]) -> List[int]:
    v: List[int] = []
    w: int = 0
    while w < len(u):
        x: str = str(u[w])
        y: bool = True
        z: int = 0
        while z < len(x):
            if (int(x[z]) % 2) == 0:
                y = False
                break  # label1 jump
            z += 1
        if y:
            v.append(u[w])
        w += 1
    return sorted(v)