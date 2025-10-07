from typing import List


def tri(k: int) -> List[int]:
    if k == 0:
        return [1]
    x: List[int] = [1, 3]
    h: int = 2
    while h <= k:
        if (h % 2) == 0:
            y: int = (h // 2) + 1
            x.append(y)
        else:
            z: int = x[h - 1] + x[h - 2] + ((h + 3) // 2)
            x.append(z)
        h += 1
    return x