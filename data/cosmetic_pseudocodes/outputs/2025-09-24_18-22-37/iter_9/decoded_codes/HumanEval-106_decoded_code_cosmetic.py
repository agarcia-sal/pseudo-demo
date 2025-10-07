from typing import List

def f(alpha: int) -> List[int]:
    beta: List[int] = []
    delta: int = 1
    while delta <= alpha:
        epsilon: int = delta % 2
        if epsilon == 0:
            zeta: int = 1
            eta: int = 1
            while eta <= delta:
                zeta *= eta
                eta += 1
            beta.append(zeta)
        else:
            theta: int = 0
            iota: int = 1
            while iota <= delta:
                theta += iota
                iota += 1
            beta.append(theta)
        delta += 1
    return beta