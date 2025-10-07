from typing import List, Optional, Tuple

def pluck(alpha: List[int]) -> List[int]:
    if not alpha:
        return []

    omega: List[int] = [x for x in alpha if x % 2 == 0]

    if not omega:
        return []

    def findMinBeta(delta: List[int], epsilon: int) -> Tuple[int, int]:
        # returns (min_value, min_index)
        zeta: int = delta[0]
        eta: int = 0
        theta: int = 1
        while theta < epsilon:
            if delta[theta] < zeta:
                zeta = delta[theta]
                eta = theta
            theta += 1
        return zeta, eta

    iota, kappa = findMinBeta(omega, len(omega))

    def findIndexLambda(nu: List[int], xi: int) -> Optional[int]:
        for rho in range(len(nu)):
            if nu[rho] == xi:
                return rho
        return None  # in case xi not found, though this should not happen per logic

    sigma: Optional[int] = findIndexLambda(alpha, iota)
    if sigma is None:
        return []

    return [iota, sigma]