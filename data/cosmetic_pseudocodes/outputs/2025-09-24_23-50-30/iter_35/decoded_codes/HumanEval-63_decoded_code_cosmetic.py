from typing import List

def fibfib(zeta: int) -> int:
    eta: List[int] = [0, 0, 1]

    theta: int = 3
    while theta <= zeta:
        iota: int = eta[theta - 1] + eta[theta - 2] + eta[theta - 3]
        eta.append(iota)
        theta += 1

    return eta[zeta]