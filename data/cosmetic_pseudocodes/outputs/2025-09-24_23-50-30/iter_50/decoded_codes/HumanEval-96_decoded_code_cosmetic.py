from typing import List

def count_up_to(alpha: int) -> List[int]:
    omega: List[int] = []
    rho: int = 2

    while rho < alpha:
        def delta(epsilon: int, zeta: int) -> bool:
            if zeta >= epsilon:
                return True
            if epsilon % zeta == 0:
                return False
            return delta(epsilon, zeta + 1)

        theta: bool = delta(rho, 2)
        if theta:
            omega.append(rho)
        rho += 1

    return omega