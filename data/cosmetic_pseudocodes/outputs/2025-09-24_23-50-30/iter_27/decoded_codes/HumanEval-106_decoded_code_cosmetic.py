from typing import List

def f(alpha: int) -> List[int]:
    beta: List[int] = []
    gamma: int = 1
    delta: int = 0
    epsilon: int = 1
    zeta: int = 0
    eta: int = 1
    theta: int = 1

    i: int = 1
    while i <= alpha:
        if i % 2 == 0:
            zeta = 1
            k = 1
            while k <= i:
                zeta *= k
                k += 1
            beta.append(zeta)
        else:
            epsilon = 0
            m = 1
            while m <= i:
                epsilon += m
                m += 1
            beta.append(epsilon)
        i += 1

    return beta