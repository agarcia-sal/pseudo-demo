from typing import List

def f(integer_n: int) -> List[int]:
    omega: List[int] = []
    for alpha in range(1, integer_n + 1):
        if alpha % 2 == 0:
            rho = 1
            psi = 1
            while psi <= alpha:
                rho *= psi
                psi += 1
            omega.append(rho)
        else:
            xi = 0
            psi = 1
            while psi <= alpha:
                xi += psi
                psi += 1
            omega.append(xi)
    return omega