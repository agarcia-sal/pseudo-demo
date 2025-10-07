from typing import Iterable

def exchange(alpha: Iterable[int], beta: Iterable[int]) -> str:
    xi = 0
    tau = 0

    for rho in alpha:
        if rho % 2 != 0:
            xi += 1

    for zeta in beta:
        if zeta % 2 == 0:
            tau += 1

    return "YES" if tau >= xi else "NO"