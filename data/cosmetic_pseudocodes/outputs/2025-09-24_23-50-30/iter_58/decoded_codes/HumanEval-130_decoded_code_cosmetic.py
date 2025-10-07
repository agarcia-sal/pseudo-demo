from typing import List

def tri(omega: int) -> List[int]:
    if omega == 0:
        return [1]
    sigma: List[int] = [1, 3]
    delta = 2
    while delta <= omega:
        if delta % 2 == 0:
            sigma.append((delta // 2) + 1)
        else:
            sigma.append(sigma[delta - 1] + sigma[delta - 2] + ((delta + 3) // 2))
        delta += 1
    return sigma