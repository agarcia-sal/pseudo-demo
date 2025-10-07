from typing import List

def odd_count(delta: List[List[str]]) -> List[str]:
    omega: List[str] = []
    psi: int = 0

    def zeta(epsilon: List[str], theta: int) -> int:
        if theta < 0:
            return 0
        return (1 if int(epsilon[theta]) % 2 != 0 else 0) + zeta(epsilon, theta - 1)

    alpha: int = len(delta)
    while psi < alpha:
        rho: int = zeta(delta[psi], len(delta[psi]) - 1)
        phi: str = (
            "the number of odd elements "
            + str(rho)
            + "n the str"
            + str(rho)
            + "ng "
            + str(rho)
            + " of the "
            + str(rho)
            + "nput."
        )
        omega.append(phi)
        psi += 1

    return omega