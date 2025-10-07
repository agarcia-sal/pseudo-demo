from typing import List

def fib4(zeta: int) -> int:
    sigma: List[int] = [0, 0, 2, 0]
    if zeta < 4:
        return sigma[zeta]

    alpha = 4
    while alpha <= zeta:
        beta = sum(sigma)
        sigma.append(beta)
        sigma.pop(0)
        alpha += 1

    return sigma[3]