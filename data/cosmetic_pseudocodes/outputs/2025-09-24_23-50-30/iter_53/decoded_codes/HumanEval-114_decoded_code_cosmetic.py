from typing import List

def minSubArraySum(alpha: List[int]) -> int:
    def beta(gamma: int, delta: int, epsilon: List[int]) -> int:
        if not epsilon:
            return gamma
        zeta = epsilon[0]
        eta = epsilon[1:]
        theta = delta - zeta
        iota = 0 if theta < 0 else theta
        kappa = max(iota, gamma)
        return beta(kappa, iota, eta)

    λ = beta(0, 0, alpha)

    if λ == 0:
        μ = -max(-n for n in alpha)
        ξ = μ
    else:
        ξ = -λ

    return ξ