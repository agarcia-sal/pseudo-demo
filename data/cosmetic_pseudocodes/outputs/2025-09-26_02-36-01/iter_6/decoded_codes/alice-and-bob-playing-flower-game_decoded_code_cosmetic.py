class Solution:
    def flowerGame(self, gamma: int, delta: int) -> int:
        zeta = ((gamma - 1) // 2) + 1
        eta = gamma - zeta
        theta = ((delta - 1) // 2) + 1
        iota = delta - theta
        kappa = (zeta * iota) + (eta * theta)
        return kappa